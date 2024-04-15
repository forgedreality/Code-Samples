# Nanoleaf interface
import keyboard
import nanocommunicator
import json
import asyncio
import random
import colorsys
import layouthelper

stop_loop = False

def rand(min, max):
    return random.randint(min, max)


#for rgb
async def getColors():
    colors = [0] * 3
    for c in range(len(colors)):
        colors[c] = rand(0, 255)
    return colors


# for hsb
async def colorPicker():
    hue = rand(0, 359)
    sat = rand(30, 100)
    bright = rand(50, 100)
    c = [hue, sat, bright]
    return c


async def set_brightness(controller, brightness):
    # {'brightness': {'value': 100, 'max': 100, 'min': 0}, 'colorMode': 'effect', 'ct': {'value': 2700, 'max': 6500, 'min': 1200}, 'hue': {'value': 0, 'max': 360, 'min': 0}, 'on': {'value': True}, 'sat': {'value': 0, 'max': 100, 'min': 0}}
    # {'brightness': {'value': 100, 'max': 100, 'min': 0}, 'colorMode': 'hs', 'ct': {'value': 2700, 'max': 6500, 'min': 1200}, 'hue': {'value': 15, 'max': 360, 'min': 0}, 'on': {'value': True}, 'sat': {'value': 100, 'max': 100, 'min': 0}}
    status = {"brightness":{"value": brightness},"duration":0,"sat":{"value":100}}
    status = json.dumps(status)
    await nanocommunicator.make_request("put", [controller.ip, controller.token, controller.endpoints["state"], status])

    # [4, 120, 165]
    outClr = [255, 160, 0]
    # print(str(outClr))
    mult = 255/100
    mod = round(mult*brightness)
    # Vary color of text based on brightness slider value
    res = str([outClr[0] - (outClr[0] - mod), outClr[1] - round((outClr[0] - mod) / 2), outClr[2] + (outClr[0] - mod)])
    return f'Set {controller.name} brightness to ß{res}{brightness}ß.'


async def check_values(controllers):
    t = []
    for c in controllers:
        if not isinstance(c, str):
            if controllers[c].get():
                t.append(c)

    if len(t) == 0:
        return "ERROR: No controllers selected."

    return t


async def calcBrightness(red, green, blue, brightness):
    # sourceAvg = (red + green + blue) / 3
    brightCalc = ((red*299)+(green*587)+(blue*114))/1000
    brightPct = round(brightCalc/255*100)
    diff = brightPct - brightness
    # print(diff)
    adjAmt = diff/3

    if diff <= 0:
        return [round(red+adjAmt), round(green+adjAmt), round(blue+adjAmt)]

    return [round(red-adjAmt), round(green-adjAmt), round(blue-adjAmt)]


async def shut_down(controller, brightness, **kwargs):
    # Have the ability to pass in on="true" or on="false"
    o = "" if len(kwargs) == 0 or 'on' not in kwargs else str(kwargs['on']).lower() if str(kwargs['on']).lower() == "true" or str(kwargs['on']).lower() == "false" else ""
    if o == "":
        status = await nanocommunicator.get_status(controller)
        cmd = 'false' if status["on"]["value"] is True else 'true'

    else:
        cmd = o

    payload = "{\"on\":{\"value\": " + cmd + "}}"
    if cmd == 'false':
        # Fix for Nanoleaf firmware bug that causes the panels to relight when an animation loops
        await set_brightness(controller=controller, brightness=0)
        await nanocommunicator.make_request("put", [controller.ip, controller.token, controller.endpoints["state"], payload])
    else:
        # No need to send the 'on' request when setting brightness
        await set_brightness(controller=controller, brightness=int(brightness.get()))

    return f"{controller.name} turned {'on' if cmd == 'true' else 'off'}."


async def build_ids(controller):
    ids = []
    for i in controller.ids:
        ids.append(i)
    return ids


# Pick a random scene from those stored on controller.
async def choose_scene(controller, brightness = 100):
    await set_brightness(controller=controller, brightness=int(brightness.get()))
    effects = await nanocommunicator.get_effects(controller)
    selectedEffect = random.choice(effects)

    json_data = {
        "select" : selectedEffect
    }

    payload = json.dumps(json_data)

    await nanocommunicator.make_request("put", [controller.ip, controller.token, controller.endpoints["effects"], payload])
    return f"Selected {selectedEffect} on {controller.name}."


# Fill with random color
async def color_fill(controller, brightness = 100, color = []):
    b = (brightness if type(brightness) == int else round(brightness.get()))
    if len(color) == 3:
        hue = color[0]
        sat = color[1]
        bright = color[2]
    else:
        t = await colorPicker()
        hue = t[0]
        sat = t[1]
        bright = t[2]


    json_data = {
        "on": {
            "value": True
        },
        "brightness": {
            "value": bright if b == 0 else b,
            "duration": 0
        },
        "hue": {
            "value": hue
        },
        "sat": {
            "value": sat
        },
        "colorMode": "hs"
    }

    payload = json.dumps(json_data)

    rgbcnvt = colorsys.hsv_to_rgb(hue/360, sat/100, bright/100)
    rgbout = f"[{round(rgbcnvt[0]*255)}, {round(rgbcnvt[1]*255)}, {round(rgbcnvt[2]*255)}]"

    await nanocommunicator.make_request("put", [controller.ip, controller.token, controller.endpoints["state"], payload])
    return f"Set color fill (ß{rgbout}hue: {hue}, saturation: {sat}, brightness: {bright}ß) on {controller.name}"
    # return f"Set color fill (hue: {hue}, saturation: {sat}, brightness: {bright}) on {controller.name}"


# Build a random colorfading animation
'''
                     * - Total panels
                     |  * - Panel ID
                     |  | * - Total frames
                     |  | |  [*******] - RGB values
                     |  | |  |   |   |   * - White LED.  Always 0.  Currently ignored by Nanoleaf API.
                     |  | |  |   |   |   | * - Transition time; 1 = 100ms
                     |  | |  |   |   |   | |  [R G  B   W T ] - Frame 2 ...more frames follow...
                     |  | |  |   |   |   | |  |  |  |   | |       * - Next Panel ID
                     |  | |  |   |   |   | |  |  |  |   | |       | * - Total frames
                     |  | |  |   |   |   | |  |  |  |   | |       | | [*****] - RGBWT...
        "animData": "27 1 35 255 233 214 0 15 57 32 231 0 15 ...
'''
# array push function builds write command string

async def build_animation(controller, brightness, solidColor, offsetColors):
    # fix brightness
    if brightness == None or brightness == 0:
        brightness = 100

    await set_brightness(controller=controller, brightness=brightness)

    animSequence = ""
    tileIds = controller.ids

    totalSequences = len(tileIds)
    totalTransitions = rand(10,75)

    # set up color arrays
    srcColors_r = []
    srcColors_g = []
    srcColors_b = []

    altColors_r = []
    altColors_g = []
    altColors_b = []

    dstColors_r = []
    dstColors_g = []
    dstColors_b = []

    n_frames = rand(50, 250)

    # create color array for each transition
    for c in range(totalTransitions):
        src_r = rand(0, 255)
        src_g = rand(0, 255)
        src_b = rand(0, 255)

        alt_r = rand(0, 255)
        alt_g = rand(0, 255)
        alt_b = rand(0, 255)

        srcColors_r.append(src_r)
        srcColors_g.append(src_g)
        srcColors_b.append(src_b)

        altColors_r.append(alt_r)
        altColors_g.append(alt_g)
        altColors_b.append(alt_b)

    animSequence = str(totalSequences)

    for i in tileIds:
        animSequence += " " + str(i) + " " + str(totalTransitions)
        for t in range(totalTransitions):
            dstColors_r = altColors_r[t] if offsetColors and i in controller.offset_ids else srcColors_r[t]
            dstColors_g = altColors_g[t] if offsetColors and i in controller.offset_ids else srcColors_g[t]
            dstColors_b = altColors_b[t] if offsetColors and i in controller.offset_ids else srcColors_b[t]

            # Adjust colors for brightness slider
            if brightness < 100:
                adjusted = await calcBrightness(red=dstColors_r, green=dstColors_g, blue=dstColors_b, brightness=brightness)

                dstColors_r = adjusted[0]
                dstColors_g = adjusted[1]
                dstColors_b = adjusted[2]

            if not solidColor:
                # choose whether or not to slightly shift panel color
                shouldIChange = rand(0, 1)
                # if changing, decide whether to go up or down
                addOrSub = rand(0, 1)
                #if changing, decide by how much for all three color channels
                cngAmount = rand(10, 45)

                if shouldIChange:
                    if addOrSub:
                        dstColors_r = max(5, (altColors_r[t] if offsetColors and i in controller.offset_ids else srcColors_r[t]) - cngAmount)
                        dstColors_g = max(5, (altColors_g[t] if offsetColors and i in controller.offset_ids else srcColors_g[t]) - cngAmount)
                        dstColors_b = max(5, (altColors_b[t] if offsetColors and i in controller.offset_ids else srcColors_b[t]) - cngAmount)
                    else:
                        dstColors_r = min(255, (altColors_r[t] if offsetColors and i in controller.offset_ids else srcColors_r[t]) + cngAmount)
                        dstColors_g = min(255, (altColors_g[t] if offsetColors and i in controller.offset_ids else srcColors_g[t]) + cngAmount)
                        dstColors_b = min(255, (altColors_b[t] if offsetColors and i in controller.offset_ids else srcColors_b[t]) + cngAmount)

            # add transition variation
            animSequence += " " + str(dstColors_r) + " " + str(dstColors_g) + " " + str(dstColors_b) + " " + "0" + " " + str(n_frames)

    json_data = {
        "write": {
            "animData": animSequence,
            "loop": True,
            "animType": "custom",
            "version": "2.0",
            "command": "display",
            "palette": []
        }
    }

    payload = json.dumps(json_data)

    await nanocommunicator.make_request("put", [controller.ip, controller.token, controller.endpoints["effects"], payload])
    return f"Sent animation sequence to {controller.name}. \n  --Total transitions: {totalTransitions} \n  --Transitions frames: {n_frames}"


async def wander_animation(controller, brightness, mode, solidColor, offsetColors, darkMode, reverseMode):
    # modes = ["Sequential", "Waterfall", "Yo-yo", "Burst"]
    # Waterfall/Burst
    if int(mode) == 1 or int(mode) == 3:
        l = await nanocommunicator.get_layout(controller)
        layout = await layouthelper.calculate_panel_adjacency(l, waterfall = True, reversed = (True if int(mode)== 3 else False))

    # Yo-yo
    elif int(mode) == 2:
        layout = [[i] for i in controller.ids]
        r = []
        for i in layout:
            r.insert(0, i)
        layout = r + layout if reverseMode else layout + r

    else:
        layout = [[i] for i in controller.ids]

    if reverseMode:
        r = []
        for i in layout:
            r.insert(0, i)
        layout = r

    '''
    {'numPanels': 14, 'sideLength': 150, 'positionData': [{'panelId': 1, 'x': 299, 'y': 303, 'o': 300, 'shapeType': 0}, {'panelId': 2, 'x': 299, 'y': 389, 'o': 120, 'shapeType': 0}, {'panelId': 3, 'x': 374, 'y': 433, 'o': 300, 'shapeType': 0}, {'panelId': 15, 'x': 374, 'y': 519, 'o': 0, 'shapeType': 0}, {'panelId': 5, 'x': 224, 'y': 259, 'o': 240, 'shapeType': 0}, {'panelId': 6, 'x': 224, 'y': 173, 'o': 180, 'shapeType': 0}, {'panelId': 7, 'x': 149, 'y': 129, 'o': 120, 'shapeType': 0}, {'panelId': 8, 'x': 149, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 9, 'x': 74, 'y': 0, 'o': 120, 'shapeType': 0}, {'panelId': 10, 'x': 149, 'y': 303, 'o': 60, 'shapeType': 0}, {'panelId': 11, 'x': 74, 'y': 259, 'o': 0, 'shapeType': 0}, {'panelId': 12, 'x': 0, 'y': 303, 'o': 300, 'shapeType': 0}, {'panelId': 13, 'x': 149, 'y': 389, 'o': 120, 'shapeType': 0}, {'panelId': 14, 'x': 74, 'y': 433, 'o': 60, 'shapeType': 0}]}
    [{'panelId': 12, 'x': 0, 'y': 129, 'o': 300, 'shapeType': 0}, {'panelId': 11, 'x': 74, 'y': 86, 'o': 0, 'shapeType': 0}, {'panelId': 6, 'x': 224, 'y': 0, 'o': 180, 'shapeType': 0}, {'panelId': 10, 'x': 149, 'y': 129, 'o': 60, 'shapeType': 0}, {'panelId': 5, 'x': 224, 'y': 86, 'o': 240, 'shapeType': 0}, {'panelId': 14, 'x': 74, 'y': 259, 'o': 60, 'shapeType': 0}, {'panelId': 13, 'x': 149, 'y': 216, 'o': 120, 'shapeType': 0}, {'panelId': 1, 'x': 299, 'y': 129, 'o': 300, 'shapeType': 0}, {'panelId': 2, 'x': 299, 'y': 216, 'o': 120, 'shapeType': 0}, {'panelId': 3, 'x': 374, 'y': 259, 'o': 300, 'shapeType': 0}, {'panelId': 15, 'x': 374, 'y': 346, 'o': 0, 'shapeType': 0}]
    '''
    # fix brightness
    if brightness == None or brightness == 0:
        brightness = 100

    await set_brightness(controller=controller, brightness=brightness)

    # Format is: number of panels, followed by a definition of each panel, and all of its frames of animation.
    # Each panel can have its own varying number of frames.
    # Looks like this:
    # [#_of_panels] {
    #   [panel_id_1] {
    #     [#_of_frames] {
    #       r g b w t; r g b w t; r g b w t ... for # of frames
    #     }
    #   }
    #   [panel_id_2] {
    #     [#_of_frames] {
    #       r g b w t; r g b w t; r g b w t ... for # of frames
    #     }
    #   }
    #   ... for # of panels
    # }
    animSequence = ""
    tileIds = controller.ids
    # tileIds = layout
    frameCounter = layout.copy()
    # Add final frame to hide slight pause between loops, but not for Yo-yo mode
    if mode != 2:
        frameCounter.append([-1])

    # Should be number of tiles on controller
    totalSequences = len(tileIds)

    # set up color arrays
    srcColors_r = [0] * 2
    srcColors_g = [0] * 2
    srcColors_b = [0] * 2

    altColors_r = [0] * 2
    altColors_g = [0] * 2
    altColors_b = [0] * 2

    # create colors for panels and wanderer
    # 0 = wanderer, 1 = all others
    srcColors_r[0] = rand(0, 255)
    srcColors_g[0] = rand(0, 255)
    srcColors_b[0] = rand(0, 255)
    srcColors_r[1] = rand(0, 255)
    srcColors_g[1] = rand(0, 255)
    srcColors_b[1] = rand(0, 255)

    # offset panels
    altColors_r[0] = rand(0, 255)
    altColors_g[0] = rand(0, 255)
    altColors_b[0] = rand(0, 255)
    altColors_r[1] = rand(0, 255)
    altColors_g[1] = rand(0, 255)
    altColors_b[1] = rand(0, 255)

    animSequence = str(totalSequences)

    # Controls the speed of the animation
    frame_transitions = str(rand(0,2))
    # frame_transitions = str(1)

    for i in tileIds:
        animSequence += f" {str(i)} {str(len(frameCounter))}"
        for t in frameCounter:
            altColors = True if offsetColors and i in controller.offset_ids else False
            # If i == t, we're looking at the wanderer
            # else we're looking at any other panel
            dstColor_r = altColors_r[0 if i in t else 1] if altColors else srcColors_r[0 if i in t else 1]
            dstColor_g = altColors_g[0 if i in t else 1] if altColors else srcColors_g[0 if i in t else 1]
            dstColor_b = altColors_b[0 if i in t else 1] if altColors else srcColors_b[0 if i in t else 1]
            # dstColor_r = altColors_r[0 if i == t else 1] if altColors else srcColors_r[0 if i == t else 1]
            # dstColor_g = altColors_g[0 if i == t else 1] if altColors else srcColors_g[0 if i == t else 1]
            # dstColor_b = altColors_b[0 if i == t else 1] if altColors else srcColors_b[0 if i == t else 1]

            if darkMode and not i in t:
                dstColor_r = max(0, dstColor_r - (round(((brightness*.60)/100)*255)))
                dstColor_g = max(0, dstColor_g - (round(((brightness*.60)/100)*255)))
                dstColor_b = max(0, dstColor_b - (round(((brightness*.60)/100)*255)))
            # Adjust colors for brightness slider
            # if brightness < 100:
                # adjusted = await calcBrightness(red=dstColor_r, green=dstColor_g, blue=dstColor_b, brightness=0.5 if darkMode else brightness)

                # dstColor_r = adjusted[0]
                # dstColor_g = adjusted[1]
                # dstColor_b = adjusted[2]

            if not solidColor and i != t:
                # choose whether or not to slightly shift panel color
                shouldIChange = rand(0, 1)
                # if changing, decide whether to go up or down
                addOrSub = rand(0, 1)
                #if changing, decide by how much for all three color channels
                cngAmount = rand(5, 30)

                if shouldIChange:
                    if addOrSub:
                        dstColor_r = max(5, dstColor_r - cngAmount)
                        dstColor_g = max(5, dstColor_g - cngAmount)
                        dstColor_b = max(5, dstColor_b - cngAmount)
                    else:
                        dstColor_r = min(255, dstColor_r + cngAmount)
                        dstColor_g = min(255, dstColor_g + cngAmount)
                        dstColor_b = min(255, dstColor_b + cngAmount)

            # add transition variation
            # Adds a single frame as fix to disguise pause between loops
            animSequence += f" {dstColor_r} {dstColor_g} {dstColor_b} 0 {frame_transitions}"

    json_data = {
        "write": {
            "animData": animSequence,
            "loop": True,
            "animType": "custom",
            "version": "2.0",
            "command": "display",
            "palette": []
        }
    }

    payload = json.dumps(json_data)

    await nanocommunicator.make_request("put", [controller.ip, controller.token, controller.endpoints["effects"], payload])
    return f"Sent wanderer sequence to {controller.name}."


# Loop specifies if should loop or not.  Expects boolean.  Optional.
async def random_colors(controller, brightness, loop = False, panel_ids = [], color_r = 0, color_g = 0, color_b = 0):
    # fix brightness
    await set_brightness(controller=controller, brightness=brightness)

    global stop_loop
    if stop_loop:
        stop_loop = False
        return f"Stopping loop."

    end_key = "left_shift"

    ids = panel_ids
    # set up list of IDs through which to iterate
    if len(ids) == 0:
        ids = await build_ids(controller)
        print(f"Looping commands on {controller.name}.  To stop, press {end_key}.")


    # avoid grays
    if (color_r == color_g == color_b):
        color_r = rand(0, 255)
        color_g = rand(0, 255)
        color_b = rand(0, 255)

    # choose whether or not to slightly shift panel color
    shouldIChange = rand(0, 1)
    # if changing, decide whether to go up or down
    addOrSub = rand(0, 1)
    #if changing, decide by how much for all three color channels
    cngAmount = rand(10, 45)

    if shouldIChange:
        if addOrSub:
            color_r = max(1, (color_r - cngAmount))
            color_g = max(1, (color_g - cngAmount))
            color_b = max(1, (color_b - cngAmount))
        else:
            color_r = min(255, (color_r + cngAmount))
            color_g = min(255, (color_g + cngAmount))
            color_b = min(255, (color_b + cngAmount))

    # concat colors together for json payload
    colors = str(color_r) + " " + str(color_g) + " " + str(color_b)
    transition_time = str(rand(0, 2))

    # pick a random panel
    random_id = random.choice(ids)

    json_data = {
        "write": {
            "command": "display",
            "animType": "static",
            "colorType": "RGB",
            "colorMode": "effect",
            "animData": "1 " + str(random_id) + " 1 " + colors + " 0 " + transition_time,
            "loop": "false"
        }
    }

    payload = json.dumps(json_data)

    await nanocommunicator.make_request("put", [controller.ip, controller.token, controller.endpoints["effects"], payload])

    # remove it from the list to prevent choosing same again
    ids.remove(int(random_id))

    await asyncio.sleep(0.1)

    if keyboard.is_pressed(end_key) or stop_loop:
        stop_loop = True
        return f"\nExiting..."

    elif len(ids) > 0 or loop is True:
        if len(ids) == 0:
            color_r = color_g = color_b = 0

        task = asyncio.create_task(random_colors(
            controller=controller,
            brightness=brightness,
            loop=loop,
            panel_ids=ids,
            color_r=color_r,
            color_g=color_g,
            color_b=color_b
        ))

        await task

    return f"Finished loop on {controller.name}."


# Loop specifies if should loop or not.  Expects boolean.  Optional.
async def dynamic_color(controller, brightness, solidColor, offsetColors, color = [], color2 = []):
    # fix brightness
    await set_brightness(controller=controller, brightness=brightness)

    # set up list of IDs through which to iterate
    ids = await build_ids(controller)

    srcColors = color if color else await getColors()
    srcColors2 = color2 if color2 else await getColors()
    dstColors = [0,0,0]

    itr = 0
    animStr = ""

    for i in ids:
        clrString = ""

        if offsetColors and i in controller.offset_ids:
            dstColors[0] = srcColors2[0]
            dstColors[1] = srcColors2[1]
            dstColors[2] = srcColors2[2]
        else:
            dstColors[0] = srcColors[0]
            dstColors[1] = srcColors[1]
            dstColors[2] = srcColors[2]

        # Adjust colors for brightness slider
        if brightness < 100:
            adjusted = await calcBrightness(red=dstColors[0], green=dstColors[1], blue=dstColors[2], brightness=brightness)

            dstColors[0] = adjusted[0]
            dstColors[1] = adjusted[1]
            dstColors[2] = adjusted[2]


        itr += 1

        if not solidColor:
            # choose whether or not to slightly shift panel color
            shouldIChange = rand(0, 1)
            # if changing, decide whether to go up or down
            addOrSub = rand(0, 1)
            #if changing, decide by how much for all three color channels
            cngAmount = rand(10, 75)

            if shouldIChange:
                if addOrSub:
                    dstColors[0] = max(5, (srcColors2[0] if offsetColors and i in controller.offset_ids else srcColors[0]) - cngAmount)
                    dstColors[1] = max(5, (srcColors2[1] if offsetColors and i in controller.offset_ids else srcColors[1]) - cngAmount)
                    dstColors[2] = max(5, (srcColors2[2] if offsetColors and i in controller.offset_ids else srcColors[2]) - cngAmount)
                else:
                    dstColors[0] = min(255, (srcColors2[0] if offsetColors and i in controller.offset_ids else srcColors[0]) + cngAmount)
                    dstColors[1] = min(255, (srcColors2[1] if offsetColors and i in controller.offset_ids else srcColors[1]) + cngAmount)
                    dstColors[2] = min(255, (srcColors2[2] if offsetColors and i in controller.offset_ids else srcColors[2]) + cngAmount)

        # concat colors together for json payload
        clrString = str(dstColors[0]) + " " + str(dstColors[1]) + " " + str(dstColors[2])
        transition_time = str(rand(0, 10))

        animStr += str(i) + " 1 " + clrString + " 0 " + transition_time + (" " if itr < len(ids) else "")

    json_data = {
        "write": {
            "command": "display",
            "animType": "static",
            "colorType": "RGB",
            "colorMode": "effect",
            "animData": str(len(ids)) + " " + animStr,
            "loop": "false"
        }
    }

    payload = json.dumps(json_data)

    await nanocommunicator.make_request("put", [controller.ip, controller.token, controller.endpoints["effects"], payload])

    await asyncio.sleep(0.01)

    return f"Sent command to {controller.name}, based on ß{srcColors}{srcColors}ß{(f' and ß{srcColors2}{srcColors2}ß' if offsetColors else '')}."


# {{IP}}:16021/api/v1/{{auth_token}}
# controller = nanoleaf2
# controller_ip = controller.ip
# controller_token = controller.token
# endpoint = effectsList

async def init_brightness(controller, brightness):
    task = asyncio.create_task(set_brightness(controller=controller, brightness=int(brightness.get())))
    return await task


async def custom_anim(controller, brightness, solidColor, offsetColors):
    task = asyncio.create_task(build_animation(controller=controller, brightness=int(brightness.get()), solidColor=solidColor.get(), offsetColors=offsetColors.get()))
    return await task


async def wander_anim(controller, brightness, mode, solidColor, offsetColors, darkMode, reverseMode):
    task = asyncio.create_task(wander_animation(controller=controller, brightness=int(brightness.get()), mode=mode.get(), solidColor=solidColor.get(), offsetColors=offsetColors.get(), darkMode=darkMode.get(), reverseMode=reverseMode.get()))
    return await task


async def loop_colors(controller, brightness, infinite_loop):
    task = asyncio.create_task(random_colors(controller=controller, brightness=int(brightness.get()), loop=infinite_loop.get()))
    return await task


async def single_color(controller, brightness, solidColor, offsetColors, color=[], color2=[]):
    task = asyncio.create_task(dynamic_color(controller=controller, brightness=brightness.get(), solidColor=solidColor.get(), offsetColors=offsetColors.get(), color=color, color2=color2))
    return await task

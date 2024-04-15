# Build from this file
import main
from tkinter import *
from nanoleaf import Nanoleaf
from scrolltext import ScrollTxtArea
import asyncio
import nanocommunicator

nanoleaf1 = Nanoleaf(
    ip="192.168.50.141",
    auth_token="YBmu0Vaqu3fqeXzzzzz9ZjQ3kmU2lVzW",
    name="Mega",
    offset_ids=[14, 15, 16, 22, 23, 24, 25]
)

nanoleaf2 = Nanoleaf(
    ip="192.168.50.176",
    auth_token="Z12ezzzzzvY39OVIaVrir3yCVMnwefeJ",
    name="Diamond",
    offset_ids=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
)

nanoleaf3 = Nanoleaf(
    ip="192.168.50.185",
    auth_token="6dUXMBLWIXCUnCFLYzzzzzjEOb5OXfYa",
    name="Cornerstar",
    offset_ids=[11, 12, 13, 14, 15]
)

nanoleaf4 = Nanoleaf(
    ip="192.168.50.194",
    auth_token="gTHiLyKpzzzzzjCkx4zraLjCtGxTvGsS",
    name="Whit Nano",
    checked_by_default=False
)

panels = [nanoleaf1, nanoleaf2, nanoleaf3, nanoleaf4]
# panels = [nanoleaf1, nanoleaf2, nanoleaf3]

# Set properties on all controllers to assist future requests
for p in panels:
    ids = []
    l = asyncio.run(nanocommunicator.get_layout(p))

    for d in l["positionData"]:
        ids.append(d["panelId"])
    p.set_ids(ids)

root = Tk()
root.title("Nanoleaf Master Control")
root.iconbitmap("./images/icon.ico")

loopcheck = BooleanVar()
solidColor = BooleanVar()
offsetColors = BooleanVar()
unifiedColor = BooleanVar()
unifiedColor2 = BooleanVar()
brightness = DoubleVar()
wMode = DoubleVar()
reverseMode = DoubleVar()
darkMode = DoubleVar()
textcolor = "#0478a5"
mainbgcolor = "#eee"
mainfgcolor = "#fce3ae"
accentcolor = "#666"

root.resizable(width=FALSE, height=FALSE)
# root.geometry("900x600+120+120")
# root.geometry("500x550")
root.config(bg=mainbgcolor)

checked = {}
for p in enumerate(panels):
    checked[p[1]] = BooleanVar()

for c in checked:
    checked[c].set(c.checked_by_default)

def hover(parent, color):
    parent.config(bg=color)
    for child in parent.winfo_children():
        if not isinstance(child, Button):
            child.config(bg=color)

main_frame = Frame(root, border=0)
main_frame.grid()
main_frame.grid_columnconfigure(0, weight=1)

select_frame = Frame(root, border=1, relief=GROOVE, bg=mainbgcolor)
select_frame.grid(sticky=EW)
select_frame.grid_columnconfigure(0, weight=1)

power_frame = Frame(root, border=1, relief=GROOVE, bg=mainbgcolor)
power_frame.grid(sticky=EW)
for i in range(12):
    power_frame.grid_columnconfigure(i, weight=1)

loop_frame = Frame(root, border=1, relief=GROOVE, bg=mainbgcolor)
loop_frame.grid(sticky=EW)
loop_frame.grid_columnconfigure(0, weight=1)

wanderModes = ["Sequential", "Waterfall", "Yo-yo", "Burst"]
wander_frame = Frame(root, border=1, relief=GROOVE, bg=mainbgcolor)
wander_frame.grid(sticky=EW)
# for c in range(1, len(wanderModes)+1):
#     wander_frame.grid_columnconfigure(c, weight=1)

color_frame = Frame(root, border=1, relief=GROOVE, bg=mainbgcolor)
color_frame.grid(sticky=EW)
color_frame.grid_columnconfigure(0, weight=1)

fill_frame = Frame(root, border=1, relief=GROOVE, bg=mainbgcolor)
fill_frame.grid(sticky=EW)
fill_frame.grid_columnconfigure(0, weight=1)

anim_frame = Frame(root, border=1, relief=GROOVE, bg=mainbgcolor)
anim_frame.grid(sticky=EW)
anim_frame.grid_columnconfigure(0, weight=1)

status_box = Frame(root, border=1, relief=RAISED, bg="#fff")
status_box.grid(sticky=EW, columnspan=1)
status_box.grid_columnconfigure(0, weight=1)

quit_frame = Frame(root, border=1, relief=GROOVE, bg=mainbgcolor)
quit_frame.grid(sticky=EW)
quit_frame.grid_columnconfigure(0, weight=1)

main_label = Label(main_frame, text="Control panel to maximize your Nanoleaf life!", padx=20, pady=20, font=('Arial 15 bold'))
main_label.grid(column=0, row=0, columnspan=1)

select_label = Label(select_frame, text=f"Select Nanoleaf controller", padx=5, pady=5, font=('Arial 12'))
select_label.grid(column=0, row=0, columnspan=len(checked))


def createCheckbox(parent, text, var, col, row):
    check = Checkbutton(parent, text=text, padx=10, pady=2, fg=textcolor, variable=var, width=12, anchor=W, justify='left', onvalue=True, offvalue=False)
    check.grid(column=col, row=row, sticky=W, padx=10)
    return check


class CB(Frame):
    def __init__(self, parent, panel, col):
        self.parent = parent
        self.panel = panel
        self.col = col
        Frame.__init__(self, parent)
        self.check_var = BooleanVar()
        check = Checkbutton(self, text=f"Nanoleaf {panel.name}", padx=5, pady=2, justify='left', variable=self.check_var, onvalue=True, offvalue=False, fg=textcolor, command=lambda: self.checkBoxes(), width=18)

        # Use checked_by_default property to determine if checkbox starts out checked
        check.select() if panel.checked_by_default else check.deselect()
        check.grid(column=self.col, row=1)

    def get(self):
        return self.panel

    def checkBoxes(self):
        global checked

        frame = self.parent
        namevar = self.panel
        value = self.check_var.get()
        checked[namevar].set(value)


for panel in checked:
    p = CB(parent=select_frame, panel=panel, col=list(checked.keys()).index(panel))
    p.grid(column=p.col, row=1)
    # giving each column the same weight balances their widths
    select_frame.grid_columnconfigure(p.col, weight=1)


async def call_func(controllers, func_name, **kwargs):
    c = await main.check_values(controllers)
    if type(c) == list:
        tasks = []
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        for p in c:
            tasks.append(func_name(controller=p, **kwargs))

        res = await asyncio.gather(*tasks)
        for r in res:
            statusText.update(r)

        return None

    return statusText.update(c)


# Not working
# def call_func_loop(checked, loopcheck):
#     statusText.update(f"\nStarting loop on {i.name for i in checked}")
#     asyncio.run(main.loop_colors(checked, loopcheck))

powerButton = Button(power_frame, text="Toggle power", command=lambda: asyncio.run(call_func(checked, main.shut_down, brightness=brightness)), fg=textcolor, bg="#fff", padx=15, pady=15, relief=GROOVE, bd=2, width=15)
powerButton.grid(column=0, row=0, sticky=W, pady=8, padx=10, rowspan=3)

brightSlider = Scale(power_frame, variable=brightness, from_=1, to=100, sliderlength=50, showvalue=0, resolution=1, troughcolor=accentcolor, fg=textcolor, bg=mainbgcolor, label="Brightness", bd=1, orient=HORIZONTAL)
brightSlider.grid(column=1, row=0, sticky=EW, columnspan=11)
brightSlider.set(100)
brightSlider.configure(command=lambda x: asyncio.run(call_func(checked, main.init_brightness, brightness=brightness)))
for i in range(0, 101, 10):
    t = ("" if i > 0 else "       ") + str(i) + ("    " if 100 == i else "")
    brightLabel = Label(power_frame, text=t, fg=textcolor)
    brightLabel.grid(column=int(i/10)+1, row=2, sticky=W)

sceneButton = Button(power_frame, text="Select random scene", command=lambda: asyncio.run(call_func(checked, main.choose_scene, brightness=brightness)), fg=textcolor, bg="#fff", padx=15, pady=15, relief=GROOVE, bd=2, width=15)
sceneButton.grid(column=12, row=0, sticky=E, pady=8, padx=10, rowspan=3)

animButton = Button(loop_frame, text="Build colorfade animation", command=lambda: asyncio.run(call_func(checked, main.custom_anim, brightness=brightness, solidColor=solidColor, offsetColors=offsetColors)), fg=textcolor, bg="#fff", padx=15, pady=15, relief=GROOVE, bd=2)
animButton.grid(column=0, row=0, sticky=W, pady=8, padx=10, rowspan=2)

solidColorCheck = createCheckbox(loop_frame, "Solid color", solidColor, 1, 0)
offsetColorsCheck = createCheckbox(loop_frame, "Offset colors", offsetColors, 1, 1)

wandererButton = Button(wander_frame, text="Wanderer animation", command=lambda: asyncio.run(call_func(checked, main.wander_anim, brightness=brightness, mode=wMode, solidColor=solidColor, offsetColors=offsetColors, darkMode=darkMode, reverseMode=reverseMode)), fg=textcolor, bg="#fff", padx=15, pady=15, relief=GROOVE, bd=2)
wandererButton.grid(column=0, row=0, sticky=W, pady=8, padx=10, rowspan=3)

wanderModeSlider = Scale(wander_frame, variable=wMode, from_=0, to=len(wanderModes)-1, sliderlength=50, showvalue=0, resolution=1, troughcolor=accentcolor, fg=textcolor, bg=mainbgcolor, label="Mode", bd=1, orient=HORIZONTAL)
wanderModeSlider.grid(column=1, row=0, sticky=EW, rowspan=2, columnspan=len(wanderModes))
wanderModeSlider.set(0)
for m in wanderModes:
    wander_label = Label(wander_frame, text=m, fg=textcolor)
    wander_label.grid(column=wanderModes.index(m)+1, row=2, sticky=W)

# for c in range(wander_frame.grid_size()[0] - 1):
#     wander_frame.grid_columnconfigure(c, weight=1)

reversedCheck = createCheckbox(wander_frame, "Reversed", reverseMode, len(wanderModes)+1, 0)
darkModeCheck = createCheckbox(wander_frame, "Dark mode", darkMode, len(wanderModes)+1, 1)
solidColorCheck = createCheckbox(wander_frame, "Solid color", solidColor, len(wanderModes)+2, 0)
offsetColorsCheck = createCheckbox(wander_frame, "Offset colors", offsetColors, len(wanderModes)+2, 1)

colorButton = Button(color_frame, text="Single color shift", command=lambda: asyncio.run(call_func(checked, main.single_color, brightness=brightness, solidColor=solidColor, offsetColors=offsetColors, color=asyncio.run(main.getColors()) if unifiedColor.get() else [], color2=asyncio.run(main.getColors()) if unifiedColor.get() else [])), fg=textcolor, bg="#fff", padx=15, pady=15, relief=GROOVE, bd=2)
colorButton.grid(column=0, row=0, sticky=W, pady=8, padx=10, rowspan=3)

solidColorCheck = createCheckbox(color_frame, "Solid color", solidColor, 1, 0)
offsetColorsCheck = createCheckbox(color_frame, "Offset colors", offsetColors, 1, 1)
unifiedColorCheck = createCheckbox(color_frame, "Unified base", unifiedColor, 1, 2)

fillButton = Button(fill_frame, text="Random color fill", command=lambda: asyncio.run(call_func(checked, main.color_fill, brightness=brightness, color = asyncio.run(main.colorPicker()) if unifiedColor2.get() else [])), fg=textcolor, bg="#fff", padx=15, pady=15, relief=GROOVE, bd=2)
fillButton.grid(column=0, row=0, sticky=W, pady=8, padx=10, rowspan=1)

unifiedColorCheck = createCheckbox(fill_frame, "Unified base", unifiedColor2, 1, 0)
unifiedColorCheck.select()

loopButton = Button(anim_frame, text="Start loop (experimental)", command=lambda: asyncio.run(call_func(checked, main.loop_colors, brightness=brightness, infinite_loop=loopcheck)), fg=textcolor, bg="#fff", padx=15, pady=15, relief=GROOVE, bd=2)
loopButton.grid(column=0, row=0, sticky=W, pady=8, padx=10)

infiniteCheck = createCheckbox(anim_frame, "Run forever?", loopcheck, 1, 0)

statusText = ScrollTxtArea(root = status_box, height = len(checked))
statusText.update("Ready...")

quitButton = Button(quit_frame, text="Close tool", command=root.quit, fg=textcolor, bg="#fff", padx=10, pady=5, relief=GROOVE, bd=2)
quitButton.grid(column=0, row=0, pady=8, padx=10, sticky=EW)

buttons = [powerButton, sceneButton, fillButton, loopButton, colorButton, animButton, wandererButton, quitButton]
for b in buttons:
    b.bind("<Enter>", lambda event: event.widget.config(bg=textcolor, fg="#fff"))
    b.bind("<Leave>", lambda event: event.widget.config(bg="#fff", fg=textcolor))

frames = [loop_frame, wander_frame, color_frame, fill_frame, anim_frame, quit_frame]
for f in frames:
    f.bind("<Enter>", lambda event: hover(event.widget, mainfgcolor))
    f.bind("<Leave>", lambda event: hover(event.widget, mainbgcolor))

root.mainloop()
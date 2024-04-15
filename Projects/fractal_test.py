import turtle
import random
import math
import asyncio, threading

screen_width = 800
screen_height = 600

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.right(angle)


def rand_draw(pen, min_dist, max_dist, w, h, iter, start_color):
    if max_dist - min_dist < 1 or iter < 1: return 1

    t_clr = [None] * len(pen)
    curr_clr = [None] * len(pen)
    c_change = [None] * len(pen)

    for i in range(len(pen)):
        t_clr[i] = (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255))
        curr_clr[i] = [start_color[0], start_color[1], start_color[2]]
        c_change[i] = [
            (t_clr[i][0] - start_color[i][0]) / iter,
            (t_clr[i][1] - start_color[i][1]) / iter,
            (t_clr[i][2] - start_color[i][2]) / iter
        ]

    for i in range(iter):
        for j, v in enumerate(pen):
            x,y = v.pos()

            mx = random.randint(min_dist, max_dist)
            my = random.randint(min_dist, max_dist)

            dx = max( min( x + (mx * (-1 if random.randint(0, 1) else 1)), w ), -w )
            dy = max( (min( y + (my * (-1 if random.randint(0, 1) else 1)), h )), -h )

            v.setheading(math.degrees(math.atan2((dx - x), (dy - y))))

            v.goto(dx, dy)

            curr_clr[j][0] = int(start_color[j][0] + (c_change[j][0] * i))
            curr_clr[j][1] = int(start_color[j][1] + (c_change[j][1] * i))
            curr_clr[j][2] = int(start_color[j][2] + (c_change[j][2] * i))

            pen[j].pencolor((curr_clr[j][0], curr_clr[j][1], curr_clr[j][2]))

    pen.hideturtle()

    return 0


async def main():
    num_pens = 20
    iterations = 10000

    min_dist = 1
    max_dist = 8

    t = [None] * num_pens
    r_clr = [None] * num_pens

    for p in range(num_pens):
        t[p] = turtle.Turtle()
        t[p].speed("fastest")  # set the turtle's speed to its maximum value

        r_clr[p] = (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255))

    # set up the turtle's screen
    screen = t[0].getscreen()
    screen.bgcolor("black")  # set the background color to black
    screen.colormode(255)  # allow colors to be given as 0-255 RGB values
    screen.setup(screen_width, screen_height)

    sw = round(screen_width / 2)
    sh = round(screen_height / 2)
    tasks = [None] * num_pens

    for i, p in enumerate(t):
        p.hideturtle()
        p.pencolor(r_clr[i])  # set the turtle's pen color
        p.pensize(1)  # set the turtle's pen size to 1 pixel
        p.penup()
        p.goto(random.randint(-sw, sw), random.randint(-sh, sh))
        p.setheading(random.randint(0,359))
        p.showturtle()
        p.pendown()

    rand_draw(t, min_dist, max_dist, sw, sh, iterations, r_clr)

    # draw a Koch curve of order 5
    # koch(t, 5, 500)
    # rand_draw(t, 1, 10, sw, sh, (sw * sh) / 4, color_b)

    screen.exitonclick()


'''
async def rand_draw(pen, min_dist, max_dist, w, h, iter, start_color):
    print(f"running {pen}")
    if max_dist - min_dist < 1 or iter < 1: return 1

    t_clr = (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255))
    curr_clr = [start_color[0], start_color[1], start_color[2]]
    c_change = []

    c_change = [
        (t_clr[0] - start_color[0]) / iter,
        (t_clr[1] - start_color[1]) / iter,
        (t_clr[2] - start_color[2]) / iter,
    ]

    for i in range(iter):
        x,y = pen.pos()

        mx = random.randint(min_dist, max_dist)
        my = random.randint(min_dist, max_dist)

        dx = max( min( x + (mx * (-1 if random.randint(0, 1) else 1)), w ), -w )
        dy = max( (min( y + (my * (-1 if random.randint(0, 1) else 1)), h )), -h )

        pen.setheading(math.degrees(math.atan2((dx - x), (dy - y))))

        pen.goto(dx, dy)

        curr_clr[0] = int(start_color[0] + (c_change[0] * i))
        curr_clr[1] = int(start_color[1] + (c_change[1] * i))
        curr_clr[2] = int(start_color[2] + (c_change[2] * i))

        pen.pencolor((curr_clr[0], curr_clr[1], curr_clr[2]))

    pen.hideturtle()

    return 0


async def main():
    num_pens = 8
    iterations = 50

    min_dist = 1
    max_dist = 8

    t = [None] * num_pens
    r_clr = [None] * num_pens

    for p in range(num_pens):
        t[p] = turtle.Turtle()
        t[p].speed("fastest")  # set the turtle's speed to its maximum value

        r_clr[p] = (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255))

    # set up the turtle's screen
    screen = t[0].getscreen()
    screen.bgcolor("black")  # set the background color to black
    screen.colormode(255)  # allow colors to be given as 0-255 RGB values
    screen.setup(screen_width, screen_height)

    sw = round(screen_width / 2)
    sh = round(screen_height / 2)
    # tasks = [None] * num_pens

    for i, p in enumerate(t):
        p.hideturtle()
        p.pencolor(r_clr[i])  # set the turtle's pen color
        p.pensize(1)  # set the turtle's pen size to 1 pixel
        p.penup()
        p.goto(random.randint(-sw, sw), random.randint(-sh, sh))
        p.setheading(random.randint(0,359))
        p.showturtle()
        p.pendown()
        # tasks[i] = asyncio.create_task(rand_draw(p, min_dist, max_dist, sw, sh, iterations, r_clr[i]))
        # tasks.append(asyncio.create_task(rand_draw(p, min_dist, max_dist, sw, sh, iterations, r_clr[i])))

    tasks = [asyncio.create_task(rand_draw(p, min_dist, max_dist, sw, sh, iterations, r_clr[i])) for i, p in enumerate(t)]
    await asyncio.gather(*tasks)


    # draw a Koch curve of order 5
    # koch(t, 5, 500)
    # rand_draw(t, 1, 10, sw, sh, (sw * sh) / 4, color_b)

    screen.exitonclick()
'''

asyncio.run(main())

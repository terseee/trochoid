import math
import turtle


def get_count(ext_radius, in_radius):
    count = 1
    while ext_radius * count % in_radius != 0:
        count = count + 1
    return ext_radius * count / in_radius


def get_trochoid(ext_radius, in_radius, h):
    trochoid = []
    i = 0
    count = get_count(ext_radius, in_radius)
    limit = count * 360
    while i < limit:
        psi = (i * math.pi) / 180;
        x = (ext_radius - in_radius) * math.cos(psi) + h * math.cos(((ext_radius + in_radius) / ext_radius) * psi)
        y = (ext_radius - in_radius) * math.sin(psi) - h * math.sin(((ext_radius + in_radius) / ext_radius) * psi)
        trochoid.append((x, y))
        i = i + 1
    return trochoid


def draw(center_x, center_y, ext_radius, in_radius, h):
    t = turtle.Turtle()
    trochoid = get_trochoid(ext_radius, in_radius, h)
    t.color('purple')
    first = True
    for x, y in trochoid:
        if first:
            t.up()
            first = False
        else:
            t.down()
        t.goto(center_x + x, center_y + y)
    turtle.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ext_radius = int(input('Enter external radius: '))
    in_radius = int(input('Enter internal radius: '))
    h = int(input('Enter height for the drawing point: '))

    draw(0, 50, ext_radius, in_radius, h)

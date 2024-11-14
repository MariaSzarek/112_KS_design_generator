import turtle

SPEED = 10


def offset(x, y, scale):
    offset_x = x / 2 * scale
    offset_y = y / 2 * scale
    return (offset_x, offset_y)


def draw_points(points, offset, scale):
    t = turtle.Turtle()
    t.speed(SPEED)
    t.penup()
    t.goto(points[0][0] * scale - offset[0], points[0][1] * scale - offset[1])
    for point in points:
        t.pendown()
        t.goto(point[0] * scale - offset[0], point[1] * scale - offset[1])
        t.dot(5)


def draw_coordinates(points, offset, scale):
    t = turtle.Turtle()
    t.speed(SPEED)
    for point in points:
        t.penup()
        t.goto(point.x * scale - offset[0], point.y * scale - offset[1] - 20)
        t.pendown()
        t.write(f"({point.x}, {point.y})", align="center")


def draw_building(x, y, scale):
    t = turtle.Turtle()
    t.speed(SPEED)
    t.penup()
    t.goto(-x * scale / 2, -y * scale / 2)
    t.pendown()
    for i in range(2):
        t.forward(x * scale)
        t.left(90)
        t.forward(y * scale)
        t.left(90)
    t.penup()

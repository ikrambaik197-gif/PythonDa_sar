import turtle
import math

# =========================
# SETUP
# =========================
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# =========================
# FUNGSI LINGKARAN
# =========================
def circle(radius, color_fill, color_line="black", pensize=3):
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.pensize(pensize)
    t.color(color_line, color_fill)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# =========================
# RING LUAR
# =========================
circle(300, "black", "white", 3)
circle(250, "#2f437a", "black", 3)

# =========================
# BINTANG
# =========================
def draw_star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

draw_star(-220, 0, 40)
draw_star(180, 0, 40)

# =========================
# TEKS MELINGKAR
# =========================
def curved_text(text, radius, start_angle):
    t.penup()
    t.goto(0, 0)
    t.setheading(start_angle)

    for char in text:
        angle = 360 / (len(text) * 2.2)
        t.right(angle)
        t.forward(radius)
        t.setheading(t.towards(0,0) - 90)
        t.write(char, align="center", font=("Arial", 18, "bold"))
        t.backward(radius)
        t.setheading(start_angle - angle)

curved_text("SEKOLAH MENENGAH KEJURUAN", 275, 90)
curved_text("PRESTASI PRIMA", 275, -90)

# =========================
# TANGAN MERAH
# =========================
t.penup()
t.goto(-60, -120)
t.setheading(0)
t.pendown()
t.pensize(8)
t.color("black", "red")
t.begin_fill()

# Telapak
t.forward(120)
t.left(90)
t.forward(180)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)

# Jari telunjuk
t.left(90)
t.forward(40)
t.left(90)
t.forward(200)
t.right(90)
t.forward(40)
t.right(90)
t.forward(200)

t.end_fill()

# Lingkaran atas jari (tombol)
t.penup()
t.goto(0, 200)
t.pendown()
t.pensize(6)
t.color("black")
t.circle(40)

turtle.done()
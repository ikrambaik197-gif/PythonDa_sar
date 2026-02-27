import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Gambar Rumah")

t = turtle.Turtle()
t.speed(3)
t.pensize(2)

# ======================
# Badan Rumah
# ======================
t.penup()
t.goto(-100, -50)
t.pendown()
t.fillcolor("lightyellow")
t.begin_fill()
for i in range(2):
    t.forward(200)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()

# ======================
# Atap
# ======================
t.penup()
t.goto(-120, 100)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.goto(0, 200)
t.goto(120, 100)
t.goto(-120, 100)
t.end_fill()

# ======================
# Pintu
# ======================
t.penup()
t.goto(-30, -50)
t.pendown()
t.fillcolor("saddlebrown")
t.begin_fill()
for i in range(2):
    t.forward(60)
    t.left(90)
    t.forward(90)
    t.left(90)
t.end_fill()

# ======================
# Jendela Kiri
# ======================
t.penup()
t.goto(-80, 20)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for i in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

# ======================
# Jendela Kanan
# ======================
t.penup()
t.goto(40, 20)
t.pendown()
t.begin_fill()
for i in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

turtle.done()
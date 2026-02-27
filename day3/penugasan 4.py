import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Fibonacci Tree")

t = turtle.Turtle()
t.left(90)          # Menghadap ke atas
t.speed(0)         # Kecepatan maksimum
t.color("brown")
t.pensize(2)

# Fungsi rekursif Fibonacci Tree
def fibonacci_tree(n, length):
    if n <= 0:
        return
    
    # Gambar batang
    t.forward(length)
    
    # Simpan posisi & arah
    posisi = t.pos()
    arah = t.heading()
    
    # Cabang kiri
    t.left(30)
    fibonacci_tree(n-1, length * 0.7)
    
    # Kembali ke posisi awal cabang
    t.penup()
    t.setpos(posisi)
    t.setheading(arah)
    t.pendown()
    
    # Cabang kanan
    t.right(30)
    fibonacci_tree(n-2, length * 0.7)
    
    # Kembali ke posisi awal batang
    t.penup()
    t.setpos(posisi)
    t.setheading(arah)
    t.backward(length)
    t.pendown()

# Pindah ke bawah layar
t.penup()
t.goto(0, -250)
t.pendown()

# Panggil fungsi (ubah angka untuk tingkat kerumitan)
fibonacci_tree(8, 80)

turtle.done()
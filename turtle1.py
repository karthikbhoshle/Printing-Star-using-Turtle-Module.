import turtle
s=turtle.Screen()
t=turtle.Turtle()

s.bgcolor('black')
t.pencolor('orange')
st=['red','green']
t.speed(0)
a=10
i=0
while True:
      t.pencolor(st[i])
      i=(i+1)%2


      t.forward(a)
      a+=5

      t.right(150)
      if a==650:
        break


t.forward(a/2)
t.ht()
turtle.done()
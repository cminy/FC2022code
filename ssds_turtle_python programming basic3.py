import turtle as t
import numpy as np
import beepy
import time
import random

m = t.Turtle()
m.shape('classic')

#  template
t.bgcolor('aqua')
m.up() # 그리지 않고 이동만 하는 것은 up
m.speed(0)
m.goto(0, 240) # goto : 절대좌표
m.write('Turtle race',  False, "center", ("Verdana", 36, 'normal'))

# race : x = (-300,300), y = (-200, 200)
m.goto(-300, 200)
m.down()
m.color('midnightblue')
m.begin_fill()
for i in range(2):
    m.forward(600)
    m.right(90) # 오른쪽 회전
    m.forward(400)
    m.right(90)
m.end_fill()

# draw start - finish line
m.color('white')
m.up()
m.goto(-270, 220)
m.down()
m.goto(-270, -220)
m.up()
m.goto(270, 220)
m.down()
m.goto(270, -220)

# draw gide lines
m.up()
m.goto(-300, -180)
m.down()
m.goto(300, -180)
m.up()
m.goto(-300, 180)
m.down()
m.goto(300, 180)

# draw race lines
start_ycor = np.linspace(-150, 150, 5)
race_ycor = start_ycor - 30
for i in race_ycor[1:6]:
    m.up()
    m.goto(-300, i)
    m.color('aqua')
    m.down()
    m.goto(300, i)
m.hideturtle()

# turtle
color_list = ['yellow', 'red', 'green', 'white', 'hotpink']
turtles = []
for i in range(5):
    new_turtle = t.Turtle()
    new_turtle.up()
    new_turtle.shape('turtle')
    new_turtle.color(color_list[i])
    new_turtle.goto(-290, start_ycor[i]-10)
    new_turtle.write(i+1, font=("",12,""))
    new_turtle.goto(-270, start_ycor[i])
    turtles.append(new_turtle)

# betting
n = t.Turtle()
usr_choice = int(t.textinput("turtle race", "choose your turtle"))
n.up()
n.goto(0, -290)
n.color('black')
n.write(f'{usr_choice}번 거북이를 선택하였습니다.', True, 'center', ("Verdana", 30, 'normal'))
n.hideturtle()

# race start ready
beepy.beep(sound=5)
time.sleep(0.005)
beepy.beep(sound=5)

# race start
game_over = False
while not game_over:
    for i, v in enumerate(turtles):
        rand_speed = random.randint(1, 10)
        v.fd(rand_speed)
        if v.xcor() >= 270:
            winner = i+1
            game_over = True

# result
n.clear() # 지우고 다시 쓰기
n.up()
n.goto(0, -290)
n.color('black')
if winner == usr_choice:
    result = '이겼습니다!'
else:
    result = f'졌습니다... 우승은 {winner}번 거북이!'
n.write(f'당신의 거북이가 {result}', True, 'center', ("Verdana", 30, 'normal'))

t_rank = []
for i, v in enumerate(turtles):
    t_rank.append([v.xcor(), v.ycor(), i+1])
t_rank.sort(reverse=True)
for i, v in enumerate(t_rank[:3]):
    n.goto(310, v[1])
    n.write(f'{i+1}등!')
# m.done()
t.exitonclick()

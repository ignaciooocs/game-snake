import turtle
import time
import random

screen = turtle.Screen()
screen.title('mucha calle como pa que la achiquen')
screen.bgcolor('#000')
screen.setup(width=800, height=600)
screen.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.shape('square')
player.color('#f51')
player.penup()
player.goto(0, 0)
player.direction = 'stop'

comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('#f55')
comida.penup()

comida.goto(0, 100)
comida.direction = 'stop'

segmentos = []

texto = turtle.Turtle()
texto.speed(0)
texto.color('#fff')
texto.hideturtle()
texto.penup()
texto.goto(0, 260)
texto.write('Score: 0       HighScore: 0', align='center',
            font=('Courier', 16, 'normal'))

def up():
  if player.direction != 'down':
    player.direction = 'up'

def down():
  if player.direction != 'up':
    player.direction = 'down'

def left():
  if player.direction != 'right':
    player.direction = 'left'

def right():
  if player.direction != 'left':
    player.direction = 'right'

def mov():
  if player.direction == 'up':
    y = player.ycor()
    player.sety(y+20)
  if player.direction == 'down':
    y = player.ycor()
    player.sety(y-20)
  if player.direction == 'left':
    x = player.xcor()
    player.setx(x-20)
  if player.direction == 'right':
    x = player.xcor()
    player.setx(x+20)

screen.listen()
screen.onkeypress(up, 'Up')
screen.onkeypress(down, 'Down')
screen.onkeypress(left, 'Left')
screen.onkeypress(right, 'Right')

score = 0
highscore = 0
while True:
  screen.update()
  if player.ycor() < -280 or player.ycor() > 280 or player.xcor() < -390 or player.xcor() > 390:
    score = 0
    texto.clear()
    texto.write(f'Score: {score}       HighScore: {highscore}',
                align='center',  font=('Courier', 16, 'normal'))
    time.sleep(1)
    player.goto(0, 0)
    player.direction = 'stop'
    for segmento in segmentos:
      segmento.goto(1000, 1000)
    segmentos.clear()

  if player.distance(comida) < 20:
    x = random.randint(-380, 380)
    y = random.randint(-280, 260)
    comida.goto(x, y)

    score += 1
    if score > highscore:
      highscore = score
    texto.clear()

    texto.write(f'Score: {score}       HighScore: {highscore}',
                align='center',  font=('Courier', 16, 'normal'))

    body = turtle.Turtle()
    body.speed(0)
    body.shape('square')
    body.color('#27ff67')
    body.penup()

    segmentos.append(body)

  leng = len(segmentos)
  for index in range(leng - 1, 0, -1):
    x = segmentos[index - 1].xcor()
    y = segmentos[index - 1].ycor()
    segmentos[index].goto(x, y)
  if leng > 0:
    x = player.xcor()
    y = player.ycor()
    segmentos[0].goto(x, y)

  mov()

  for segmento in segmentos:
    if segmento.distance(player) < 20:
      score = 0
      texto.clear()
      texto.write(f'Score: {score}       HighScore: {highscore}',
                  align='center',  font=('Courier', 16, 'normal'))
      time.sleep(1)
      player.goto(0, 0)
      player.direction = 'stop'
      for segmento in segmentos:
        segmento.goto(1000, 1000)
      segmentos.clear()
  time.sleep(0.08)

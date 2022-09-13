import turtle
from typing import Text

#Window initalisation
wn = turtle.Screen()
wn.title('My Game')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)        

score_a = 0
score_b = 0

class Object(turtle.Turtle):
    
    borderh = 290
    borderw = 390
    
    def __init__(self, speed, shape, shapesizeh_shapesizew, color, goto):
        super().__init__()
        (h, w) = shapesizeh_shapesizew
        self.speed(speed)
        self.shape(shape)
        self.shapesize(stretch_len=w, stretch_wid=h)
        self.color(color)
        self.penup()
        self.goto(goto)
    
    def up(self):
        y = self.ycor()
        y += 20
        self.sety(y)
    
    def down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
            
        
class TextObject(turtle.Turtle):
    def __init__(self, speed, color, goto):
        super().__init__()
        self.speed(speed)
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(goto)
    
    def Text(self, text, pos: str):
        self.write(text, align=pos, font=('Courier', 24, 'normal'))
        
class BallObject(Object):
    def __init__(self, speed, shape, shapesizeh_shapesizew, color, goto):
        super().__init__(speed, shape, shapesizeh_shapesizew, color, goto)
    
    def setd(self, dx, dy):
        self.dx = dx
        self.dy = dy
        
    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)
    
    def setBorder(self):
        global score_a
        global score_b
        if self.ycor() > self.borderh:
            self.sety(self.borderh)
            self.dy *= -1
        
        if self.ycor() < -self.borderh:
            self.sety(-self.borderh)
            self.dy *= -1
        
        if self.xcor() > self.borderw:
            self.goto(0, 0)
            self.dx *= -1
            score_a += 1
            print(score_a)
            pen.clear()
            pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))
            
        if self.xcor() < -self.borderw:
            self.goto(0, 0)
            self.dx *= -1
            score_b += 1
            print(score_b)
            pen.clear()
            pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))
            
    def paddleCollisions(self):
        #Paddle Dimensions
        if (self.xcor() > 340 and self.xcor() < 350) and (self.ycor() < paddle_b.ycor() + 40 and self.ycor() > paddle_b.ycor() - 50):
            self.setx(340)
            self.dx *= -1
        
        #Paddle Dimensions     
        if (self.xcor() <  -340 and self.xcor() > -350) and (self.ycor() < paddle_a.ycor() + 40 and self.ycor() > paddle_a.ycor() - 50):
            self.setx(-340)
            self.dx *= -1

#Paddles
paddle_a = Object(0, 'square', (5, 1), 'white', (-350, 0))
paddle_b = Object(0, 'square', (5, 1), 'white', (350, 0))

#Ball
ball = BallObject(0, 'square', (1, 1), 'white', (0, 0))
ball.setd(2, 2)

#Pen
pen = TextObject(0, 'white', (0, 260))
pen.Text('Player A: 0  Player B: 0', 'center')
    
#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a.up, 'w')
wn.onkeypress(paddle_a.down, 's')
wn.onkeypress(paddle_b.up, 'Up')
wn.onkeypress(paddle_b.down, 'Down')

#Main Game
while True:
    wn.update()

    # Move Ball
    ball.move()
    
    #Border
    ball.setBorder()
    
    #Paddle Collisions
    ball.paddleCollisions()
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.tracer(0)

balls = []

color = ["red", "blue", "yellow", "orange", "white", "purple"]
shape = ["circle", "triangle", "square"]


for _ in range(25):
    balls.append(turtle.Turtle())

for ball in balls:
    ball.shape(random.choice(shape))
    ball.color(random.choice(color))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 325)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)


gravity = 0.09

while True:

    wn.update()
    
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity 
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        # check for wall
        if ball.xcor() > 300:
            ball.dx *= -1
            ball.da *= -1
            
        if  ball.xcor() < -300:
            ball.setx(-300)
            ball.dx *= -1
            ball.da *= -1
        
        # check for bounce
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1
        
    # check for each other
    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            #check for colition
            if balls[i].distance(balls[j]) < 27:
                temp_dx = balls[i].dx
                temp_dy = balls[i].dy
                
                balls[i].dx = balls[j].dx
                balls[i].dy = balls[j].dy
                
                balls[j].dx = temp_dx
                balls[j].dy = temp_dy
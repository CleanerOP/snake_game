import turtle 
import time
import random

turtle.register_shape("snakeHead.gif")


wn = turtle.Screen()
wn.setup(width=500, height= 500)
wn.bgcolor("black")
wn.tracer(0) 


head=turtle.Turtle()
head.shape("snakeHead.gif")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"



segments = []


x = random.randint(-230 , 230)
y = random.randint(-230 , 230)

target=turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.goto(x,y)
target.direction = "stop"

liveScore = 0

score = turtle.Turtle()
score.hideturtle()     # Hide the arrow
score.penup()          # Don't draw lines
score.goto(0, 210)     # Move to top of the screen
score.color("white")
score.write(f"Score: {liveScore}", align="center", font=("Arial", 24, "normal"))




def update_score():
    global liveScore
    liveScore += 10
    score.clear()
    score.write(f"Score: {liveScore}", align="center", font=("Arial", 24, "normal"))

def go_up():
    if head.direction !="down":
        head.direction = "up"
    
def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        if head.ycor() > 240:
            head.sety(-240)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        if head.ycor() < -240:
            head.sety(240)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        if head.xcor() < -240:
            head.setx(240)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        if head.xcor() > 240:
            head.setx(-240)


    if head.distance(target) < 20:  # safer and smoother
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        target.goto(x, y)

        update_score()

        new_segment = turtle.Turtle()
        new_segment.color("green")
        new_segment.shape("square")
        new_segment.penup()


        # Place it at the last segment’s position (or head’s if no segments yet)
        if len(segments) > 0:
            last_seg = segments[-1]
            new_segment.goto(last_seg.xcor(), last_seg.ycor())
        else:
            new_segment.goto(head.xcor(), head.ycor())

        segments.append(new_segment)





wn.listen()
wn.onkey(go_up,"Up")
wn.onkey(go_down,"Down")
wn.onkey(go_left,"Left")
wn.onkey(go_right,"Right")



while True:
       wn.update()

        # Move the segments from end to front
       for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)

       if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        # ✅ Check for collision with body
       for segment in segments[1:]:  # 👈 Skip the first segment (index 0)
            if head.distance(segment) < 20:
                # Game Over Logic
                head.goto(0, 0)
                head.direction = "stop"
                for seg in segments:
                    seg.goto(1000, 1000)  # move off-screen
                segments.clear()
                liveScore = 0
                score.clear()
                score.write("Game Over", align="center", font=("Arial", 24, "normal"))
                time.sleep(2)
                score.clear()
                score.write(f"Score: {liveScore}", align="center", font=("Arial", 24, "normal"))
                break  # optional, to stop further checking

       move()
       time.sleep(0.12)




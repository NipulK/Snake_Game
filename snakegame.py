import turtle # To create graphics and handle user input
import time # To control the speed of the game(to make the delay)
import random # To generate random numbers

delay = 0.1

# Declare the score variable
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)

wn.tracer(0)  # Turns off the screen updates    

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "up"


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segements = []

#  points
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to control the snake
def go_up():
     head.direction = "up"

def go_down():
     head.direction = "down"

def go_left():
     head.direction = "left"

def go_right():
     head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard bindings
wn.listen() # Listen for keyboard input
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "q")
wn.onkeypress(go_right, "e")

# Main game loop
while True:
    wn.update()

    if head.distance(food) < 20:

        # make the score
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Move the food to a random spot
        x = random.randint(-290, 290) # Move the food to a random spot in X axis
        y = random.randint(-290, 290)# Move the food to a random spot in Y axis
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segements.append(new_segment) # Add the new segment to the list of segments

    # Check snake and the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segements:
            segment.goto(10000, 10000) # Move the segments off the screen
        segements.clear() # Clear the segments list
   

    # Move the end segments first in reverse order
    for index in range(len(segements)-1, 0, -1): # Start from the last segment to the first segment
        x = segements[index-1].xcor() 
        y = segements[index-1].ycor()
        segements[index].goto(x, y) # Move the segment to the position of the previous segment

    # Move segment 0 to where the head is
    if len(segements) > 0: # If there is at least one segment
        x = head.xcor() 
        y = head.ycor()
        segements[0].goto(x, y)


    move()  # Function to move the snake

        # Check snake and the body
    for segement in segements:
        if segement.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segements:
                segment.goto(10000, 10000) # Move the segments off the screen
                
            segements.clear() # Clear the segments list 

            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)


wn.mainloop()
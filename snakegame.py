import turtle # To create graphics and handle user input
import time # To control the speed of the game(to make the delay)
import random # To generate random numbers

delay = 0.1

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
        # Move the food to a random spot
        x = random.randint(-290, 290) # Move the food to a random spot in X axis
        y = random.randint(-290, 290)# Move the food to a random spot in Y axis
        food.goto(x, y)

    move()  # Function to move the snake


    time.sleep(delay)


wn.mainloop()
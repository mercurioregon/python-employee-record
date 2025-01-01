
#More string stuff

#inpit gies into print.  cleaner code
# print("Hello " + input("What is your name, slick?") + "!")

# print(len(input("What is your name?")))

# username = input("Wha is your name?")

print("This is a band name generator.")
city = input("What is the name of the city you grew up in?\n")
food = input("What is one of your favorite foods?\n")
print("Your band name could be " + food + " " + city + ".")

# TIP CALCULATOR
print("Tip calculator")
billTotal = float(input("What was the total bill?"))
print(billTotal)
tipAmount = int(input("How much tip would you like to give?"))
print(tipAmount)
peopleTotal = int(input("How many people will split the bill?"))
print(peopleTotal)
grandTotal = (tipAmount /100 * billTotal + billTotal) / peopleTotal
print(f"Each person should pay: {grandTotal}")

#BASIC IF/ELSE EXERCISE:

print("welcome to the ride")
height = int(input("What is you height in inches?"))
price = 0
if height >= 48:
    print("You may ride.")
    age = int(input("What is your age? "))
    if age <= 12:
        price = 5
        print("Your ticket is $5")
    elif age <=18:
        price = 7
        print("Please pay $7")
    elif age >= 45 and age <= 55:
        price = 0
    else:
        price = 12
        print("Your ticket is $12")
    wants_photo = input("Would you like a photo? Y for yes and N for no.")
    if wants_photo == "Y":
        price += 3
    print(f"Your final price is ${price}")
else:
    print("Sorry, you may not ride.")

#ODD OR EVEN EXERCISE

# print("Odd or Even?")
# user_number = int(input("Enter a number."))
#
# if user_number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

#PRICE CALCULATOR

print("Welcome to Pizza Explosion!")
size = input("What size pizza?  S, M, or L?")
pepperoni = input("Would you like pepperoni?  Y or N")
extra_cheese = input("Would you like extra cheese?")
price = 0

if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
   price += 25
if pepperoni == "Y":
     price += 3
if extra_cheese == "Y":
    price += 2
print(f"The price of your pizza is{price}")

#TREASURE HUNT PRACTICE CODE. INCOMPLETE

print("TREASURE HUNT")
crossroad = input("You are are standing at a crossroad.  "
                  "Which direction do you go? Type L or R.").lower

if crossroad  =="L":
    print(swamp)
else:
    print(crossroad_right)
    # if swamp == "N":
    #     print(swamp_end)
    # else:
    #     print(crossroad_right)

swamp = input("You're stuck in  a swamp?  Go the other way? Y or N.").lower
swamp_end = ("You've drowned because you are stubborn and stupid.  Good job.")
crossroad_right = input("You've reached the edge of a clear lake."
                        "  There is an island in the middle. 
                         Wait for a boat, or swim for it.? Type 'swim' or 'wait'")

#IMPORTING AND RANDOMIZATION
# 
   import  random
import mymodule

random_integer = random.randint(1, 10)
print(random_integer)
print(mymodule.my_favorite_number)  


#COFFEE MACHINE CODE

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_enough(order_ingredients):
    """returns the amount of resources needed to make each drink"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough water {item}.")
            is_enough = False
    return is_enough

def process_coins():
    """returns total calculated from amount of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?:  ")) * .25
    total += int(input("How many dimes?:  ")) * .10
    total += int(input("How many nickels?:  ")) * .05
    total += int(input("How many pennies?:  ")) * .01
    return total

def is_transaction_successful(money_received, drink_cost):
     """return Truewhen payment accepted, FALSE if not"""
     if money_received >=  drink_cost:
         change = round(money_received - drink_cost, 2)
         print(f"Here is {change} in change.")
         global profit
         profit += drink_cost
         return True
     else:
         print("Not enough money.  Money refunded.")
         return False

def make_coffee (drink_name, order_ingredients):
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"Here is your coffee.")

is_on = True
while is_on:
    choice = input("What drink would you like? espresso, latte, or cappuccino?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

#OOP AND TURTLE STUFF

from  turtle import Turtle , Screen

clem =Turtle()

print(clem)
clem.shape("turtle")
clem.color("DarkGreen")
my_screen = Screen()
clem.forward(100)
my_screen.exitonclick()     

#import modules / PRETTYTABLE

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("City Name", ["Portland", "Seattle", "San Francisco"])
table.add_column("State", ["Oregon", "Washington", "California"])
table.align= "l"
print(table)

#CREATING CLASSES

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        print("new user created..")
user_1 = User("555", "Monkeyface")
user_2 = User("777", "Pancake")
print(user_2.username)

#quiz game - classes

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

new_q = Question("Bacon?", "False")
print(new_q.text)

#main

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f" Your final score is {quiz.score}/{quiz.question_number}")

#quizbrain page

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
          return self.question_number < len(self.question_list)

    def  next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q:{self.question_number}; {current_question.text}(True or False?): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Nope")
        print(f"The answer is {correct_answer}.")

#more turtle work

from turtle import Turtle, Screen

chet = Turtle()
chet.shape("turtle")
chet.color("green")

for _ in range(4):
    chet.forward(100)
    chet.right(90)

for _ in range(50):
    chet.forward(10)
    chet.up()
    chet.forward(10)
    chet.down()


# screen = Screen()
# screen.exitonclick()   

#giving an alias to an import.

# import turtle as t
# chet = t

#more turtle work


from  turtle import Turtle , Screen
import random

clem =Turtle()


colors = ["Red", "Yellow" , "Green"]
clem.shape("turtle")
clem.color("DarkGreen")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        clem.forward(100)
        clem.right(angle)

for shape_side_n in range(3, 11):
     clem.color(random.choice(colors))
     draw_shape(shape_side_n)


my_screen = Screen()
my_screen.exitonclick()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    line_color = (r, g, b)
    return line_color

#randomized colors

for _ in range(200):
    clem.color(random_color())
    clem.forward(50)
    clem.setheading(random.choice(directions))

#sprigraph with random colors

for _ in range(200):
    clem.color(random_color())
    clem.circle(100)
    current_heading = clem.heading()
    clem.setheading(current_heading + 10)

#COLRGRAM

import colorgram

colors = colorgram.extract('Hirstspotpainting.jpg', 8)


rgb_colors =  []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)


color_list  = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169)]

clem =turtle_module.Turtle()
clem.home()
clem.dot()
clem.penup()
clem.hideturtle()
clem.speed("fastest")
clem.setheading(225)
clem.fd(300)
clem.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    clem.dot(20, random.choice(color_list))
    clem.fd(50)

    if dot_count % 10 == 0:
     clem.setheading(90)
     clem.fd(50)
     clem.setheading(180)
     clem.fd(500)
     clem.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()



from turtle import Turtle, Screen

chet = Turtle()
screen = Screen()

def move_forward():
    chet.fd(10)

def move_left():
    new_heading = chet.heading() + 10
    chet.setheading(new_heading)


def move_right():
    new_heading = chet.heading() - 10
    chet.setheading(new_heading)

def move_backward():
    chet.backward(10)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_left, "a")
screen.onkey(move_right, "s")
screen.onkey(move_backward, "z")


screen.exitonclick()


#TURTLE RACE


from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Choose a color: R,G,Y,B,O, or P")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_postions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_postions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"YOU WIN! The {winning_turtle} turtle is the winner!")
            else:
                print(f"The {winning_turtle} won.  YOU LOSE!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()

    #(ABOVE FOR LOOP REPLACES ALL OF THE BELOW)

# chet = Turtle(shape="turtle")
# chet.penup()
# chet.color("blue")
# chet.goto(x=-230, y=66)
# 
# chet = Turtle(shape="turtle")
# chet.penup()
# chet.color("orange")
# chet.goto(x=-230, y=33)
# 
# chet = Turtle(shape="turtle")
# chet.penup()
# chet.color("yellow")
# chet.goto(x=-230, y=-33)
# 
# chet = Turtle(shape="turtle")
# chet.penup()
# chet.color("purple")
# chet.goto(x=-230, y=-66)
# 
# chet = Turtle(shape="turtle")
# chet.penup()
# chet.color("green")
# chet.goto(x=-230, y=-99)


screen.exitonclick()

#snake game

from turtle import Screen, Turtle
import time
from turtledemo.penrose import start

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ye Olde Snakee Gamee")
screen.tracer(0)

start_positions = [(0,0), (-20, 0), (-40,0)]

segments = []

for position in start_positions:
    new_segment = Turtle("square")
    new_segment.color ("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    for seg_number in range(len(segments) -1, 0,-1):
       new_x =  segments[seg_number - 1].xcor()
       new_y =  segments[seg_number - 1].ycor()
       segments[seg_number].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()

#snake.py is now:

from turtle import Turtle


START_POSITIONS = [(0,0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN =270
LEFT =180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in START_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color ("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
            for seg_number in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_number - 1].xcor()
                new_y = self.segments[seg_number - 1].ycor()
                self.segments[seg_number].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def  up(self):
             if self.head.heading() != DOWN:
                    self.head.setheading(UP)

    def down(self):
              if self.head.heading() != UP:
                    self.head.setheading(DOWN)

    def left(self):
             if self.head.heading() != RIGHT:
                    self.head.setheading(LEFT)

    def right(self):
                if self.head.heading() != LEFT:
                    

#food.py -

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=+.5, stretch_wid=.5)
        self.color("green")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

#scoreboard

from turtle import Turtle

ALIGNMENT =    "center"
FONT = ("Georgia", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color ("yellow")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT)

    def game_over(self):
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        self.goto(0,0)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



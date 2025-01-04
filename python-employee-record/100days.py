


print ("Hello World")


first_name = "Jim"
last_name = " Mercurio"
weight = 200
sentence = first_name + last_name + " weighs" + str(weight) + " lbs."
print (sentence)

data_type = type("nine")
print(data_type)
# ----
sentence = "Verisilimitude"

print(sentence[0:14:2])

print(sentence[5:])

sentence = "the sum of {0} + {1} is {2}".format(9, 7, 16)

print(sentence)

# ------
#new_list = [4,55,21,0,88,74,121,3,5,8]
new_list = ["butter", "cake", "dogs", "zippers", "sauce"]
#new_list.append("Caboose")
#new_list[3] = "Poop"
new_list.sort()
new_list.reverse()

print(new_list)

ist_2 =["alpha", "beta", "gamma", "zeta"]

new_list.sort()
new_list.reverse()
list_2.reverse()
final_list = new_list[:3] + list_2[:3]

print(final_list)

big_list = ["a", "b", "c", 2,4,5,["Monday", "Tuesday", "Wednesday"], 5, 7]

small_list = big_list[6][2
]
print(small_list)

# new_list = [4,55,21,0,88,74,121,3,5,8,0,0,0,0,0,0]
#
# # num_pos = new_list.index(121)
# num_pos = new_list.count(0)
# print(num_pos)


#TUPLES (Immutable strings, however nested strings can be changed)
# new_tuple = (1,2,3,4, "Oregon", "Washington", ["g", "d", "h"], 5, 55, 555)
# # new_tuple[6][1] = "x"
#
# print(new_tuple[7:10])

#DICTIONARIES
#Not position oriented. {Key : data/value}
# Call the key
#Unsortable
#.pop remove by key
#.clear

dict = {"a" : "New York" ,"b": 1000}
dict ["b"] = "Oregon"
dict ["c"] = "Washington"
print(dict)

#Booleans and comparison operators

print (11==11)
print( ("beef" == "BEEF") or (4 == 4) and True)
print(8 ==8.00)
print(7 > 8)
print( 9 >= 9)
print( 9 != 5)


cond = ( not 9==7)
print(cond)


my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]
print(my_list [0]["Bill"])

In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
# """

# my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]

# my_list[2] [0] [3]= "x"
# my_list[-2] = "television"

# $ # def friday( ):
# #     print("The last day of the work week")
# #
# # friday()

# def  badge(nickname =  "bro"):
#     print("Hello there " + nickname + ", what's up?")

# badge("Dude")

# # def  remainder (num1, num2):
# #     return num1 % num2
# #
# # remainder_value = remainder(55,4)
# # print(remainder_value)


# def new_sum(*args):
#     return sum(args)
# solution = new_sum(1,2,3,4,5,3,6,3,)
# print(solution)

# #KWARGS

# # def key_values(**kwargs):
# #         print(kwargs)
# #         print(kwargs.keys())
# #         print(kwargs.values())
# #         print(kwargs.get("party"))
# #
# # key_values(state = "Oregon", party= "Democrat")

# #MORE SCOPE EXAMPLES

# def  new_age():
#         age = 52
#         #the above is an example of data outside the scope. running this will only resolve the func below

#         def add_4_to_age(age):

#                 age = age +4
#                 #Ths defines the function.  The below line runs it. The print is converted into a string for the answer.
#                 print("ADDING METHOD: " + str(age))
#                 #Below is  data passed thru from second line in outer func
#         add_4_to_age(age)
#     #below it is run
# new_age()


def merge_lists(list1, list2):
    return list1+ list2

new_list = merge_lists(["monday", "tuesday"], ["thursday", "friday"])

print(new_list)
# list function list() -  turns whatever passes thru into a list(invidiual chars)
#  .split -  splits the elements into a new string, not the characters

# def separate (str):
#         return list(str)
#
# print (separate("this was a difficult one "))

# -------

# def multi_merge (list1, string1):
#         return list1 + string1.split() + list(string1)
#
# print (multi_merge(["Mon", "Tues", "Wed"], "The days of the week;"))

# def last_list (*args):
#         return args[-1 ]
#
# print (last_list([1,2,3,4,5], ["a", "b","c"], ["hi", "hello"]))

#CANNOT CONCATENATE STRINGS AND NUMBERS.  USE STR


# IF ELSE ELIF
# animal = "orangutan"
# if animal == "cow":
#     print("eats grass")
# elif animal == "bird":
#     print("eats worms")
# elif animal == "monkey" or animal == "orangutan":
#     print("throws poo")
# else:
#     print("unsure what animal does")

#LOOPS

# space_movies = ["star_wars", "star_trek", "serenity", "2001", "ice_pirates"]
# counter = 0
#
# for movie in  space_movies:
#     counter = counter + 1
#     sentence = str(counter) +  ") " + movie + "  is my fave sci-fi movie."
#     print(sentence)

space_movies = "This is just a string of characters in sentence form."
counter = 0

for char in space_movies:
    if char == "c":
       # break
       # continue
    counter = counter + 1
    letters = str(counter) + " " + char
    print(letters)



pass #does nothing but prevent error in code.  Used as a placeholder.


x = 2
while x < 10:
        print(x)
        x = x + 1.7 # x += 1 (SAME THING)
else:
        print("big ol' number")

#loop thru DICTIONARIES
#DEFAULT print just prints keys. /// .items prints the pair /// .values prints the value only

# employees = {"jon" : 65000, "sandy" : 67000, "marvin": 80000, "tom" : 82000}
#
# for key, value in employees.items():
#     print(key)
#     print(value)

#LOOP THRU TUPLES

employees = [("jon" , 65000), ("sandy" , 67000), ("marvin" , 80000), ("tom" ,  82000)]

for (key,value) in employees:
    print(key)

#LIST

# word  = "oregon"
# newWord  = list(word)
# print (newWord)

# for num in range(12):
#     print(num)



#ZIP

# mynum = [1,2,3,4,5,6]
# words = ["there", "are", "other", "words", "derp"]
#
# for items in zip(mynum, words):
#     print(items)

#EMUMERATE

words = ["there", "are", "other", "words", "derp"]
for item in enumerate(words):
    print(item)

list_a = ["mon", "tues", "wed", "thurs", "fri"]
list_b = [7,8,9,10,11,12,13]
# list_c = [1814, 1911, 1941, 1972, 2002, 2024]
#
# newlist = list(zip(list_a, list_b, list_c))
# print(newlist)
#
# #UNPACKING THE ZIPPED LIST
# for a,b,c in newlist:
#     print(a)
#     print(b)
#     print(c)

#LIST CHECKS MIN AND MAX

# print("sat" in list_a)

# answer = max(list_b)
# print(answer)

#RANDINT PROVIDES RAND NUMBER BUT :

#IMPORT FROM LIBRARY!!!


#from random import randint
# randomnum = randint(0,1000)
# print(randomnum)


# print(mylist)
#
# shuffle(mylist)
#
# mylist = [1,2,3,4,5,6,7,8,9,10]
#
# from random import shuffle
#

from random import shuffle
mylist = list (range(101))
shuffle(mylist)
print(mylist)


#INPUT


last_name = input("Please enter your last name.")
print(last_name +" is a very cool name.")

#.STRIP REMOVES ANY UNWANTED WHITESPACE

#INT() TO CONVERT STRING BACK TO NUMBER


# BAD CODE -- FROM EXERCISES
#
# def twelver (a,b):
# (a == 12 or b == 12 or a+b == 12):
#
#
# twelver(12,6)
#
# print(twelver())

# def sequence(num_list):
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1]  == 2 and num_list [i +2] == 3:
#             return True
#     return False
# print(sequence((1,5,2,4,7,2,1,5,1,2,3,4)))
# 
# def grow_string(str):
#     result = ""
#     for i in range(len(str)):
#         result = result + str[:i+1]
#     return result
# 
# print (grow_string("Seahawks"))

#  .POP etc, = method
#  max()   = function


#BELOW
# SELF IS AN INSTANCE OF VEHICLE
class Vehicle:

    color = "red"
    engine = "v6"
    vehicle_counter = 0
    #this is a class attribute that is applied to the vehicles below

    def __init__(self, body_type, make):
        self.vehicle_body = body_type
        self. vehicle_make = make
        Vehicle.vehicle_counter += 1

    def get_vehicle_count(self):
        return Vehicle.vehicle_counter

car1 = Vehicle("coupe", "Toyota")

car2= Vehicle("truck", "ford")

print(car2.vehicle_counter)

#importing. FROM FOLDER.FILE import CLASS

from machines.machine_stuff import Vehicle

car1 = Vehicle()

from Machine_Folder.machine_stuff import Vehicle
#
# #after importing, create a subclass. CLASS NEW CLASS(ORIGINAL CLASS)
#
class Truck(Vehicle)

#creating new Trucks means they have to have the same characteristics as the original
#Vehicle class


truck1 = Truck("pickup", "ford")
truck2 = Truck("semi", "mack")
truck3 = Truck("cube", "mistubishi")
print(truck3.get_vehicle_count)


#CLASSES AND SUBCLASSES

class Animal:
    def __init__(self, name):
        self.animal_name = name
    def eat(self):
        raise NotImplementedError("Child class should be implementing this")

class Monkey(Animal):
    def eat(self):
        print("Monkey eats bananas")

class Bird(Animal):
    def eat(self):
        print("Eats worms")

    def fly(self):
        print("Way up there")


myMonkey = Monkey("mr scoops")
myMonkey.eat()

mybird = Bird("sparky")
mybird.eat()
mybird.fly()


class Shortener:
    def  __init__(self, items):
        self.original_items = items
    def print_original_items(self):
        print(self.original_items)

class ListAndCharShortener(Shortener):
     def print_shortener_items(self):
         print(self.original_items[0:3])

class DictionaryShortener(Shortener):
    def print_shortener_items(self):
        dict = self.original_items
        counter = 0
        result_dict = {}
        for (k,v) in dict.items():
            if(counter <3):
                result_dict.update({k: v})
                counter +=1
        print(result_dict)

# myshort = ListAndCharShortener("Spell your words correctly")
# myshort.print_shortener_items()

myShortener = DictionaryShortener({1: "mudge", 2: "clem", 3: "frunk", 4: "schmilkis"})
myShortener.print_shortener_items()

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        #__something__ DUNDER METHODs.
    def  __str__(self):
        return self.name + "'s age is " + str(self.age)

bob = Employee("Bob Frink", 70)

print(bob)


# Python command line tool can read python, as well as organize and import files

# Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> tom = "hello dude"
# >>> print(tom)
# hello dude


#exercise 1 - hierarchy.  Attempt 1

class Animal:
    def __init__(self):

    def eat(self):
        raise NotImplementedError("oops")
    def move(self):
        raise NotImplementedError("oops")


class Dog(Animal):
    def eat(self):
         print("Dogs eat beef")
    def move(self):
         print("Dogs run with four legs")

class Elephant(Animal):
     def eat(self):
         print("Elephants are vegetarians, I think.")

     def move(self):
          print("Elephants walk with four legs.")


class Eagle(Animal):
      def eat(self):
            print("Eagles eat mice and insects")
      def move(self):
            print("Eagles fly.")

myDog = Dog("ollie")
myDog.eat()
myDog.move()

myElephant = Elephant("dumbo")
myElephant.eat()
myElephant.move()

myEagle = Eagle("ollie")
myEagle.eat()
myEagle.move()


#CLOSER TO CORRECT: 

class Animal:
    def __init__(self):
        print("They are all animals")

    def move(self):
        print("All animals move")

    def eat(self):
        print("All animals eat something.")


class Dog(Animal):
    def __init__(self, dog_age, dog_name):
        Animal.__init__(self)
        self.age = dog_age
        self.name = dog_name

    def move(self):
        print("Dogs run with 4 legs.")

#ERROR HANDLING. TRY / EXCEPT

def sum(num1, num2):
    try:
        #this is the code that is supposed to run
        print(num1+num2)
    except:
        #this is the error message
        print("Oops, there was an error.")

number1 = input("Enter a number")

sum(number1, 12)

#preventing errors in code.  ISINSTANCE

def sum(num1, num2):
     if isinstance((num1, int) and (num2, int)):
         print(num1 + num2)
     else:
         print("Invalid date type")

number1 = input("Enter a number")

#directory creation looks a lot like git. import os

import os
print(os.getcwd())
#get current directory

# os.chdir()
#change current directory


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

#PONG

from turtle import Turtle, Screen

screen = Screen()
screen.title("PONG")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.exitonclick()

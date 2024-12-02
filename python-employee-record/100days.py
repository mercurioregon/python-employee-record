
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
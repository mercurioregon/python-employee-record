
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


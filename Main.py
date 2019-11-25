"""
This program is to show some basic functions of Python 3.
__author__= Trinh Ngo
"""

first_last_name = input("Please enter your first and last name: ")
print("Hi" + " " + first_last_name + "! \nWelcome to Python Experience.")
print("The answer is going to be 58 if we type 'print(23+5*7)'")
print(23 + 5 * 7)
a = int(input("Enter the first number (it should be an integer): "))
b = int(input("Enter the second number (it should be an integer): "))
"""Cannot create a function to make sure the user enter integer numbers 
because we just introduce some basic functions in this part."""
addition = (a + b)
difference = (a - b)
product = (a * b)
quotient = (a / b)
print("The sum of a+b is: ", addition)
print("The difference of a-b is: ", difference)
print("The product of a*b is: ", product)
print("The quotient of a/b is:", quotient)
print(a > b)
print(a == b)
print(a != b)
x = True
y = False
print("We are going to figure out the true value of x (True) and y (False)")
print("True value of x and y is:", x and y)
print("True value of x or y is:", x or y)
print("True value of not y is:", not y)

# Exercise from Hackerrank.
# The following code lines will ask user to input the price of the items,
# which are positive numbers.
# The program will stop and output the total of all items when the user
# inputs numbers less than or equal to 0.
"""
This file is to introduce while loops and for loops
___author___= Trinh Ngo
"""

""" 
    While loop is used to iterate over a block of code as long as the test 
    expression (condition) is true.
"""
print("Now let's figure out how the functions if...else, the while loops, and "
      "for loops work!")
print("We're going to find the total of shopping items.")
total = 0
price = 1
while price > 0:
    """The condition for price has to be greater than 0."""
    price = float(input("Please enter the price of the item: "))
    total += price
    """total is the sum of the each item's price."""
print("The total of your items is: ", format(total, '.2f'))
print(
    "We can use while loops for most cases, but with for loops, we have to "
    "know how many times the code is going to run.")

# Example of for loops (Exercise Student Quiz Average Nested Loop on
# Hackerrank):
# The prompt would ask user to enter 3 student's names and 3 scores of their
# exams, and the output is their names with their average scores
for numStudent in range(1, 4):
    """
    Minimum number of students is 1.
    Maximum number of students is 3.
    """
    total = 0
    studentName = input(
        "Please enter student " + str(numStudent) + "'s name: ")
    for x in range(1, 4):
        score = float(input("Please enter score " + str(x) + ": "))
        total = total + score
    average = total / 3
    print("Name: " + studentName)
    print("Average:", format(average, '.2f'))

print(
    "The next program code is to accept the cost of two items to be purchased,"
    " then the payment amount.")
print(
    "The output is going to be a thank you message with how much change will"
    " be given if the payment amount is greater than or equal to the amount "
    "of the 2 items.")
print("If not, it would tell the user how much is still owed.")
# Get the price of the first item
price1 = float(input("Enter the cost of the first item: "))
# Get the price of the second item
price2 = float(input("Enter the cost of the second item: "))
# Get the payment amount
payment = float(input("Enter the payment amount: "))
difference = payment - price1 - price2
# Determine if customer still owes
if difference < 0:
    print("You still owe ${:,.2f}".format(-difference))

# or if change is owed
else:
    print("Thank you, your change is ${:,.2f}".format(difference))

"""
The file is to show how to create a new function.
___authors__= Trinh Ngo
"""


def get_message(user_num, rand_num):
    """Define a new function:
        parameter user_num: input from the user.
        parameter rand_num: random number from computer."""
    if user_num == rand_num:
        """Conditions of user_num and rand_num."""
        print("You picked the same number as the computer!")
    elif user_num > rand_num:
        print("Your number is higher than computer's number.")
    elif user_num < rand_num:
        print("Your number is smaller than computer's number.")


def main():
    user_num = int(input("Enter a number between 1 and 5: "))
    while user_num > 5 or user_num < 1:
        user_num = int(input("Invalid number. Please enter again: "))
    import random
    """Import function random to use for the line:
        rand_num = random.randint(1, 5)"""
    rand_num = random.randint(1, 5)
    print("Computer number:", )
    print("User number:", user_num)
    """Return the created function get_message to compare the two numbers 
    and output the result."""
    get_message(user_num, rand_num)


main()
"""Call the function main"""


# This following function shows how parameters in a def function is changed to
# arguments when the function is called.

# noinspection PyShadowingNames
def number(a):
    for a in range(0, 11, 2):
        a = str("This is an even number")
    return a


# Allen Telson helped me with the following code


def b():
    while True:
        """The lines below is to ignore inputs that are not integer and ask 
        the user to input again"""
        try:
            num1 = int(input("Please enter a random integer from 0 to 10: "))
            return num1
        except ValueError:
            """Ignore value error"""
            print("This is not an integer.")
            continue


def c(num1):
    while num1 < 0 or num1 > 10:
        """Conditions for num1"""
        num1 = int(
            input("Your number is not between 0 and 10. Please try again: "))
    if num1 % 2 == 0:
        """Recall the function number(a) and a is replaced by the argument 
        num1"""
        print(number(num1))
    elif num1 % 2 == 1:
        print("This is an odd number")


result = b()
"""Attach the function b() to result"""
c(result)
"""Call the function c() with the new argument."""

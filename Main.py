#Programmer: Trinh Ngo
#This program is to show some basic functions of Python 3

first_last_name= input("Please enter your first and last name: ")
print ("Hi"+" "+first_last_name+"! \nWelcome to Python Experience.")
print ("The answer is going to be 58 if we type 'print(23+5*7)'")
print (23+5*7)
a= int(input("Enter the first number (it should be an integer): "))
b= int(input("Enter the second number (it should be an integer): "))
sum= int(a + b)
difference= (a - b)
product= (a * b)
quotient= (a / b)
print ("The sum of a+b is: ", sum)
print ("The difference of a-b is: ", difference)
print ("The product of a*b is: ", product)
print ("The quotient of a/b is:", quotient)
print (a>b)
print (a==b)
print (a!=b)
x= True
y= False
print ("We are going to figure out the true value of x (True) and y (False)")
print ("True value of x and y is:", x and y )
print ("True value of x or y is:", x or y)
print ("True value of not y is:", not y)
print("Now let's figure out how the functions if...else, the while loops, and for loops work!")
print("We're going to find the total of shopping items.")
#
# The following code lines will ask user to input the price of the items, which are positive numbers.
# The program will stop and output the total of all items when the user inputs numbers less than or equal to 0.
total= 0
price= 1
while price>0:
    price = float(input("Please enter the price of the item: "))
    total +=price
print ("The total of your items is: ", format(total, '.2f'))
print("The next program code is to accept the cost of two items to be purchased, then the payment amount.")
print("The output is going to be a thank you message with how much change will be given if the payment amount is greater than or equal to the amount of the 2 items.")
print("If not, it would tell the user how much is still owed.")


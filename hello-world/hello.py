from datetime import date


print('Hello, world!')

# program.py
sum = 1 + 2
print(sum)
print(type(sum))

## Date & String conversion using 
print("Today's date is: " + str(date.today()))

## Command-line arguments
## sys.argv is an array or a data structure that contains many items. 
##      The first position, denoted as 0 in the array, contains the program name.
import sys
print('Hello, ' + sys.argv[0] + '!')

## Another way to pass data to the program is having the user enter the data. 
#       You can code it so the program tells the user to enter information. 
#   To capture information from the user, you'll use the input() function. 
#   The input() function takes a string as an argument and displays it to the user.

print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)
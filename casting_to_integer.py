"""
Program: cast_to_integer.py
Author: Colby Boell
Last date modified: 01/12/2022

The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""
# print that prompts user input
print('Enter a value: ')
# assigning user input to input by user
user_input = (input())

# converts string to float then to int and prints it out
print(int(float(user_input)))
"""
When the user enters any type of number we get an output of an integer
When they input a string we get an error
    --Test results--
# Input   Expected Output  Actual Output
#   12           12              12
#   43.45        43              43
#   'test'    ValueError: could not convert string to float: 'test'
"""

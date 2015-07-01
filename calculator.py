"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

user_lst = raw_input("Enter the arithmetic function you want to run and numbers to use ")

def main_calculator (lst):
    num_list = lst.split(" ")
    if num_list[0] == "q":
        return
    if num_list[0] == "add":
        print add(num_list[1], num_list[2])
    elif num_list[0] == "cube":
        print cube(num_list[1])
    elif num_list[0] == "subtract":
        print subtract(num_list[1], num_list[2])
    elif num_list[0] == "multiply":
        print multiply(num_list[1], num_list[2])
    elif num_list[0] == "square":
        print square(num_list[1])
    elif num_list[0] == "power":
        print power(num_list[1], num_list[2])
    elif num_list[0] == "mod":
        print mod(num_list[1], num_list[2])
    elif num_list[0] == "divide":
        print divide(num_list[1], num_list[2])
    else: 
        print "You entered an invalid function!"

main_calculator(user_lst)


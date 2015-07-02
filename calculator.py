"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

    
def main_calculator (lst):
    num_list = lst.split(" ")

    if (len(num_list) == 2 and num_list[1].isdigit()) or (len(num_list)==3 and (num_list[1].isdigit() and num_list[2].isdigit())):
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
    else:
        print "please try again with valid funtion and numbers"
        return
        

compute_again = "y"

while compute_again == "y":   
    main_calculator(lst = raw_input("Enter the arithmetic function you want to run and numbers to use "))
    compute_again = raw_input("do you want to computing again? (y/n) ")


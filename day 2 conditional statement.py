# -*- coding: utf-8 -*-

# Arithmatic operator 
# Created on Wed Jul 23 18:49:58 2025
# @author: Admin

# Operator | Name           | Example
# +        | Addition       | 2 + 3 → 5   
# -        | Subtraction    | 5 - 2 → 3
# *        | Multiplication | 3 * 4 → 12 
# /        | Division       | 10 / 2 → 5.0 --> gives the quotient 
# //       | Floor Division | 10 // 3 → 3 --> The result of dividing 10 by 3 is 3.333...., but floor division returns the largest integer less than or equal to the result. Therefore, the result is 3.
# %        | Modulus        | 10 % 3 → 1 --> gives the remainder
# **       | Exponentiation | 2 ** 3 → 8 --> 2 to the power of 3

# Ask the user to enter a number and print whether it is even or odd.

a = int(input("enter a number"))
if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")





# code to automate operator selection

a = int(input("enter first number"))
b = int(input("enter second number"))

print("choose any operator out of the following (+,-,,/,//,%,*):")
operator = input("enter your choice ")
if (operator in ["/", "//", "%"]) and b == 0:  
    print("division by zero is not allowed")

if operator == "+":
    print(f"{a} + {b} = {a + b}")
elif operator == "-":
    print(f"{a} - {b} = {a - b}")
elif operator == "*":
    print(f"{a} * {b} = {a * b}")
elif operator == "/":
    print(f"{a} / {b} = {a / b}")
elif operator == "//":
    print(f"{a} // {b} = {a // b}")
elif operator == "%":
    print(f"{a} % {b} = {a % b}")
elif operator == "":
    print(f"{a} ** {b} = {a ** b}")
else:
    print("invalid operator")  




#    comparision  operator 
#    Created on Wed Jul 23 18:49:58 2025
#    @author: Admim
    
    
    
    # Operator | Meaning
# ==       | Equal to
# !=       | Not equal to
# >        | Greater than
# <        | Less than
# >=       | Greater than or equal
# <=       | Less than or equal


a = int(input("Enter your marks: "))
if a >= 90:
    print("grade A")
elif a >= 80:
    print("grade B")
elif a>=70:
    print("grade C")
elif a>=60:
    print("grade D")
elif a>=50:
    print("grade E")
else:
    print("grade F")


#check if its a leap year or not
a = input("enter a year to check if its a leap year or not: ")

if a%4 == 0 and a%100 != 0:
    print(f"{a} is a leap year")
elif a%400 == 0: 
    print(f"{a} is a leap year")
else:
    print(f"{a} is not a leap year")
    
    
    
     
    
#    """
#    logical   operator 
#    Created on Wed Jul 23 18:49:58 2025
#    @author: Admin
#    """ 
   
# Operator | Meaning                 | Example
# and      | True if both are true   | x > 3 and x < 10
# or       | True if at least one is | x > 3 or x < 2
# not      | Reverses the condition  | not(x > 5)



""" and operator """

age = 20
b = 50

if age >= 18 and b < 50 :
    print("You can vote!")
else:
    print("You cannot vote.")

""" or operator """

age = 20
b = 50

if age >= 18 or b < 50:
    print("You can vote!")
else:
    print("You cannot vote.")


""" not operator """
age = 20
if not age < 18:
    print("You can vote!")
else:           
    print("You cannot vote!")
   
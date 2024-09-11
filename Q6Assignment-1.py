# Q6. How do conditional statements work in Python? Illustrate with examples.
# --> Ans: Conditional statements allow your code to make decisions based on specific conditions. 
# They help control the flow of your program, enabling it to execute different code blocks depending on whether certain conditions are met. 
# Conditions: These are expressions that evaluate to either True or False. 
# They can involve comparisons, logical operators, or function calls. 
# Code Blocks: These are blocks of code that are executed or skipped depending on whether the corresponding condition is True or False. 

#Syntax of if:
#if condition:
    # Code to execute if condition is True
# eg.
age = 25
if age >= 18:
    print("You are an adult.")

#Syntax of if-else:
# if condition:
#     # Code to execute if condition is True
# else:
#     # Code to execute if condition is False
#eg.
num = 10
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Syntax of if-elif-else:
# if condition1:
#     # Code to execute if condition1 is True
# elif condition2:
#     # Code to execute if condition2 is True
# else:
#     # Code to execute if none of the conditions are True
#eg.
grade = 85
if grade >= 90:
    print("Excellent!")
elif grade >= 80:
    print("Good job!")
else:
    print("Needs improvement.")

# Syntax of nested if else:
# if condition1:
#     if condition2:
#         # Code to execute if both conditions are True
#     else:
#         # Code to execute if condition1 is True but condition2 is False
# else:
    # Code to execute if condition1 is False
#eg.
name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter password: ")
if name == "": # name can't be an empty string
    print("Please enter valid name")
else:
    if "@" not in email: # we used a membership operator
        print("Please enter the valid email")
    else:
        if len(password) < 0:
            print("No password entered")
        elif len(password) < 6: # len() function gives the the no of elements present in the string
            print("Enter the long password")
        else:
            print("Login Successful")


#Output:
# You are an adult.
# The number is even.
# Good job!
# Enter your name: Akshay                    
# Enter your email: Piyush@124
# Enter password: 2234155
# Login Successful
# Q2. Describe the role of predefined keywords in Python and provide examples of how they are used in a program.
# --> Ans: The role of predefined keywords is very important in python, 
# since they are the basic building blocks of the programming language, 
# it defines the structure and behivaour of the programming language. 
# That predefined keywords or reserved keywords are not use as identifiers or as variable name. 
# Each keyword serves as special purpose, 
# eg, 
# print() --> prints every thing whatever we writing in it 
# input() --> use to take user input 
# type() --> to identify the datatype of the variable 
# id() --> to know the address of the particular variable

# example of how keywords are used in a program
a = int(input("Enter a number to calculate factorial : ")) # take a integer user input to calculate factorial of that input
fact = 1
for i in range(1,a+1): # use for loop to calculate the factorial
    fact *= i
print("The factorial of",a,"is ",fact) # print the facortial of the user input
#output:
#Enter a number to calculate factorial : 5
#The factorial of 5 is  120
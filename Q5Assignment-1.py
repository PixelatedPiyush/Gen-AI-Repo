# Q5. explain the concept of type casting in Python with examples.
# --> Ans: Type casting is just conversion of datatype of variable from one to another.
#eg: 
a = "44" # class 'str' 
print(a) 
print(type(a)) 
a = int(a) # conversion from class 'str' to class 'int' 
print(a) 
print(type(a)) 

# their are two types of typecasing: 
# (1) implicit typecasting and (2) explicit typecasting 
# (1) implicit typecasting: the typecasting is done automatically by python interpreter. 
# (2) explicit typecasting: this type of typecasting is done by user itself, when required.

#Output:
# 44
# <class 'str'>
# 44
# <class 'int'>

#code of typecasing
a = "5.4"
b = 2
print(float(a))
a = float(a)
print(a+b)
print("\n")

c = 3.6
c = int(c)
print(c)
print("\n")

d = 3.5
e = int(d)
print(d,e)
print("\n")

h = 2
i = str(h)
print(type(h))
print(type(i))
print(h,i)
print("\n")

j = "Ajay"
k = " Piyush"
print(j+k)
print("PW" + "-Skills")
#output:
# 5.4
# 7.4


# 3


# 3.5 3


# <class 'int'>
# <class 'str'>
# 2 2


# Ajay Piyush
# PW-Skills
# Q4. Discuss the different types of operators in Python and provide examples of how they are used.
# --> Ans: Their are seven types of operators in python: 
# 1. arithmetic operators: 
# (1)addition, 
# (2)substraction, 
# (3)Multiplicaion, 
# (4)division, 
# (5) modulo, 
# (6) Exponent, 
# (7) floor division 

# 2. Comparison operators: 
# (1)equal to, 
# (2)not equal to, 
# (3) greater than 
# (4) less than 
# (5) greater than equal to 
# (6) less than equal to 

# 3. logical operators: 
# (1) logical and, 
# (2) logical or, 
# (3) logical not 

# 4. Bitwise operators: 
# (1)Bitwise and 
# (2) Bitwise or 
# (3) Bitwise not 
# (4) Bitwise X-or 
# (5) left shift 
# (6) right shift 

# 5.Assignment operators: 
# (1) Assign (=) 
# (2) Add and assign (+=) 
# (3) substract and assign (-=) 
# (4) mulitply and assign (*=) 
# (5) Divide and assing(/=) 

# 6. membership operators: 
# (1)in 
# (2) not in 

# 7. identity operators: 
# (1) is 
# (2) is not.

#Coding implementation of all operators:
#arithmetic operators
print("Arithmetic operators")
a = 3
b = 2
print(a+b)
add = a+b # addition
print(add)
c=100
d=50
sub = c-d #substracion
print(sub)
e=50
f=4
print(e*f)# multiplication
g=21
h=4
print(g/h) #get ans in float value
print(g%h) #get remainder of the division(if g<h then return g)
k=7
l=3
print(k**l) # get exponent of k^l(7 power 3)
m = 4.33
n = 2.11
print(m//n) # get the nearest lower interger of the perticular operation
# floor means bringing the value to the lower side (eliminlate the decimal part)
print("\n")

#comparison operators
print("Comparison operators")
o = 2
p = 2
print(o==p)
print(o!=p)
q = 5
print(q!=p)
print(10>2)
print(10>=2)
print(10<2)
print(10<=10)
print("\n")

#logical opertor
print("logical operator")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(not True)
print(not False)
print("\n")

#Assignment operators
print("Assignment Operator")
r = 10
s = 5
r=r+s # r += s in r, add the value s and again assign back the updated value in the same variable i.e. r
print(r)
r -= s # r = r - s
print(r)
r *= s
print(r)
r /= s
print(r)
print("\n")

#membership operator
print("Membership operator")
t = "pw skills"
print("p" in t)
print("p" not in t)
u = "Ajay"
print("Aj" in u)
print("am" in u)
print("Ram" not in u)
print("\n")

#identity operator
print("identity operator")
v = 10
w = 12
print(v is w) # v is pointing to w -> no(False)
print(v is not w) # v is not pointing to w -> yes(True)
print(id(v))
print(id(w))
x = 12
print(w is x)   # w is pointing to x -> yes(True) coz both variable have same address
print(id(w))
print(id(x))
print(w is not x) # w is not pointing ot x -> False
y = 2
z = y
print(id(y))
print(id(z))
print(y is z) # since both have same address therefore they are same and pointing to same variable
print(y is not z)
print("\n")

print("Bitwise operators: ")
print("And bit")
print(10&10)
print(10&6)
print(17&4)
print(bin(10 ))
print("\n")

print('OR BIt')
print(3|5)
print("\n")

print("Xor Bit")
print(2^6)
print("\n")

print("Left shift")
print(5<<2)
print(5<<1)
#output:
# Arithmetic operators
# 5
# 5
# 50
# 200
# 5.25
# 1
# 343
# 2.0


# Comparison operators
# True
# False
# True
# True
# True
# False
# True


# logical operator
# True
# False
# False
# False
# True
# True
# True
# False
# False
# True


# Assignment Operator
# 15
# 10
# 50
# 10.0


# Membership operator
# True
# False
# True
# False
# True


# identity operator
# False
# True
# 11758280
# 11758344
# True
# 11758344
# 11758344
# False
# 11758024
# 11758024
# True
# False


# Bitwise operators:
# And bit
# 10
# 2
# 0
# 0b1010


# OR BIt
# 7


# Xor Bit
# 4


# Left shift
# 20
# 10
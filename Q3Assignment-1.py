# Q3. Compare and contrast mutable and immutable objects in Python with examples.
# --> Ans: Mutable Objects: Mutable objects are those whose value can be changed after its creation. 
# eg. 
# lists, dictonary, sets 
# 1) you can modify the contant in mutable objects 
# 2) If you change a mutable object, all references to that object reflect the change.

# Immutable Objects: Immutable objects are those whose value can't be changed after its creation. 
# eg. 
# tuples, strings 
# 1) Any attempt to alter an immutable object results in the creation of a new object rather than modifying the original one. 
# 2) If you try to change an immutable object, a new object is created, and the original object remains unchanged.

# code for mutable objects
list1 = [1, 2, 3]
print("Original list:", list1)
print(id(list1))
list1.append(4)
print("Modified list:", list1)
print(id(list1))
list1mod = list1 # modified version of list1
list1mod.append(5)
print("List after modifying through another reference: ",list1mod)
print(id(list1mod))
#output
#Original list: [1, 2, 3]
#132759095528256
#Modified list: [1, 2, 3, 4]
#132759095528256
#List after modifying through another reference:  [1, 2, 3, 4, 5]
#132759095528256
# here all the three lists address is not changed so it mean it is mutable objecets

# code for immutable objects
string1 = "Hello"
print("Original string:", string1)
string2 = string1 + " Physics Wallah"
print("Modified string:", string2)
print("Original string after modification attempt:", string1) # here even we did modification in string1 still the modification is not print on output screen
# from this we can understood that strings are immutbale objects
#Output:
#Original string: Hello
#Modified string: Hello Physics Wallah
#Original string after modification attempt: Hello
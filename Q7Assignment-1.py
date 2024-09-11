#Q7.Describe the different types of loops in Python and their use cases with examples.
#--> Ans: 

#for loops code:
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
for num in range(5):
    print(num)
print("\n")
#Output:
#apple
#banana
#orange
#0
#1
#2
#3
#4

# while loops code:
count = 0
while count < 5:
    print(count)
    count += 1

while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input == 'q':
        break
    print(int(user_input) ** 2)
#Output
#0
#1
#2
#3
#4
#Enter a number (or 'q' to quit): q
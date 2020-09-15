import os
#-----list-----#

# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed datatypes
my_list = [1, "Hello", 3.4]


print(my_list)
print(my_list[1])


os.system('clear')
#-----list function-----#


list_fruit = ["apple", "banana", "orange"]
print(list_fruit)

list_fruit[0] = "mango"
print(list_fruit)

list_fruit.append("mango")
print(list_fruit)

list_fruit.insert(0 , "orange")
print(list_fruit)

list_fruit.remove("orange")
print(list_fruit)

list_fruit.pop()
print(list_fruit)

list_fruit.pop(0)
print(list_fruit)

print(list_fruit.index("banana"))
print(list_fruit.index("orange"))

print(list_fruit.count("banana"))

list_fruit.clear()
print(list_fruit)



list_fruit = ["apple", "banana", "orange"]
print(list_fruit)

for fruit in list_fruit:
    print(fruit)

for x in range(len(list_fruit)) :
    print(list_fruit[x])



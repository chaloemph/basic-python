#-----dictionary-----#

# empty dictionary
my_dict = {}

# dictionary of integers
my_dict = {
    "date" : 3,
    "month" : "December",
    "year":2020
}

print(my_dict)
print(my_dict['month'])

#-----dictionary function-----#
print(my_dict.keys())
print(my_dict.values())

my_dict["day"] = "sunday"
print(my_dict)

del my_dict["month"]
print(my_dict)

for x in my_dict : 
    print(x, my_dict[x])

for y in my_dict.keys() :
    print(y)

for z in my_dict.values() :
    print(z)




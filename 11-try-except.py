#-----error invalid input-----#
# try:
#     number = int(input('enter you number ? '))
# except Exception as err:
#     print("invalid", err)



#-----error case zero division-----#
# try:
#     first = float(input('Enter first number ? :'))
#     second = float(input('Enter second number ? :'))
#     print("%d / %d = %d " %(first, second, (first/second) ))
# except ZeroDivisionError as identifier:
#     print(identifier)
# except :
#     print("invalid")


#-----Raising try except-----#
try:
    name = input("Enter your name: ")
    if name == 'mateo':
        raise Exception("Whoa! Mateo you are not allowed here")
        print(("HI ", name))
except Exception as err:
    #exception
    print ("Exception: ", err)
else:
    #success try
    print ("-----Welcome-----")
finally:
    #every action
    print ("-----END-----")



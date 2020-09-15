try:
    number = int(input('enter you number ? '))
    print(number+10)
except Exception as err:
    print("invalid", err)
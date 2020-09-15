from datetime import datetime 
y_birthdate = input('what year your birthdate ? :\n') #input as strings 
print ("my age is " , datetime.now().year - int(y_birthdate))
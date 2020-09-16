def write_file(filename, value):   
    with open(filename, "w") as f :
        f.write(value)

def read_file(filename):   
    with open(filename, "r") as f :
        print(f.read())

def write_file_file_after_olddata(filename, value):
    with open(filename, "a") as f :
        f.write(value)
        
def write_file_with_create_file(filename, value):   
    with open(filename, "w+") as f :
        f.write(value)

def read_file_with_create_file(filename):   
    with open(filename, "r+") as f :
        print(f.read())
        
def write_file_with_create_file_after_olddata(filename, value):
    with open(filename, "a+") as f :
        f.write(value)

def read_line(filename):
    with open(filename, "r") as f :
        data = f.readlines()
        for line in data:
            print(line)

# write_file("text.txt", "am super man \n")
# read_file("text.txt")
# write_file_file_after_olddata("text.txt", "\nhello")

# write_file_with_create_file("text.txt", "hello\n")
# read_file_with_create_file("text.txt")
# write_file_with_create_file_after_olddata("text.txt", "hello\n")
read_line("text.txt")
print("dasdasd")
print("dasdasd")



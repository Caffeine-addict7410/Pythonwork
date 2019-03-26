#define,print_two is a given funtion name,(*args) is like argv for funtion
def print_two(*args):#:causes indents
    arg1, arg2 = args
    print(f"arg1: {arg1}, {arg2}")

#define function with arguments
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
#define function only one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
#define function with no arguments
def print_none():
    print("I got nothin'.")
#makes args#:appear before the printed text
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("FIRST!!!!!")
print_none()
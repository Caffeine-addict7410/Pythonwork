#adds the A and B variables together
def add(a, b):
   print(f"ADDING {a} + {b}")
   return a + b
#subtracts the A and B variable together 
def subtract(a, b):
    print(f"subtracting {a} - {b}")
    return a - b
#multiplys the A and B variable together    
def multiply(a, b):
    print(f"MULTIPLYING {a} + {b}")
    return a * b
#Divides the A and B variable together
def divide(a, b):
    print(f"DIVIDE {a} / {b}")
    return a / b
    

print("Let's do some math with just funtions!")
#solves math problems using the A,B formal from before for age, height, weight, and IQ
age = add(10, 4)
height = subtract(63,2)#inches
weight = multiply(70,2)#lbs
iq = divide(200,2)#this is just the average iq
#the answers
print(f"Age: {age}, Height:{height}, Weight: {weight}, IQ: {iq}")


print("Here is a puzzle.")
#math problems :P
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what,"Can you do it by hand?")



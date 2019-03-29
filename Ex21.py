def add(a, b):
   print(f"ADDING {a} + {b}")
   return a + b

def subtract(a, b):
    print(f"subtracting {a} - {b}")
    return a - b
    
def multiply(a, b):
    print(f"MULTIPLYING {a} + {b}")
    return a * b
    
def divide(a, b):
    print(f"DIVIDE {a} / {b}")
    return a / b
    

print("Let's do some math with just funtions!")

age = add(10, 4)
height = subtract(63,2)#inches
weight = multiply(70,2)#lbs
iq = divide(100,2)#this is just the average iq

print(f"Age: {age}, Height:{height}, Weight: {weight}, IQ: {iq}")


print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what,"Can you do it by hand?")



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Simple test
assert add(10, 5) == 15
assert subtract(10, 5) == 5
assert multiply(10, 5) == 50

print("All tests passed successfully!")

##NEW 
def divide(a, b):
    return a / b

assert divide(10, 2) == 5

print("All tests passed successfully!")

## NEW 

def square(a):
    return a * a

assert square_number(5) == 25

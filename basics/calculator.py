def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y != 0:
        return x / y
    return "Error"

a = 10
b = 5

print("Add:", add(a, b))
print("Multiply:", multiply(a, b))
print("Subtract:", subtract(a, b))
print("Divide:", divide(a, b))

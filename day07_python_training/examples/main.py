age = input("Enter your age: ")
print(age, type(age))
# input() will always return whatever is input as a string, even if it's something else like an integer
# if you want to read input as something else, then it should be declared/defined otherwise

real_age = int(input("Enter your age: "))
print(real_age, type(real_age))

# Type casting vs type conversion
print(1 + 2.5) # type conversion
print(1 + int(2.5)) # type casting
print(float(1) + 2.5) # type casting

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
mul = a * b
div = a / b
sub = a - b

print("Sum: ", sum)
print("Product: ", mul)
print("Quotient: ", div)
print("Remainder: ", sub)
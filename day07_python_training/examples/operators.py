# Arithmetic operators
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Addition: ", a+b)
print("Subtraction: ", a-b)
print("Multiplication: ", a*b)
print("Division: ", a/b)

print("Modulus: ", a%b) # Returns the remainder for division, for ex 21 % 4 would be 1 since 20/4=5 and you have 1 left over
print("Exponentation: ", a**b) # a to the power of b
print("Floor division: ", a//b) # Rounds down to the nearest integer

# Shorthand for operators
print()
x=10
print("Current value for x: ", x)
x += 5
print("+= shorthand: ", x)
x -= 10
print("-= shorthand: ", x)
x *= 2
print("*= shorthand: ", x)
x /= 5
print("/= shorthand: ", x)

print()
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)

print()
print("Logical operators")
cpu = 85
memory = 90
if cpu > 80 and memory > 80:
    print("High CPU and Memory Usage")
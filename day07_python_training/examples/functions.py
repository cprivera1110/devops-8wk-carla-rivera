## Functions in python
#
## What is the purpose of functions in python?
# same as in any language, to create a reusable block of code designed to perform a certain task
# and which can be called as many times as needed
# it's useful to avoid writing the same logic over and over again

# defining the function
def greet(name): # values defined here are parameters
    print(f"Hello, Cloud trainees! Welcome {name}")

greet("Joban") # calling the function
greet("Josie") # values given here are arguments
print()

def welcome(name, role):
    print(f"Hello, cloud trainee {name}! Welcome to your role in {role}!")

# for positional arguments the order they get passed in does matter (depending on what you're trying to do)
welcome("Carla", "DevOps")
# but when defined explicitly like this it doesn't matter the position, it can be in any order
# since the values are assigned/defined explicitly
welcome(name="Lawrence", role="Cloud")
welcome(role="DevOps", name="Calvin")
print()

def deploy(env="dev"):
    print(f"Deploying to environment {env}")

deploy() # call the function with default parameter
deploy("prod") # call the function with a specific argument
print()

# Variable length positional arguments
# for when you don't know how many arguments you're going to get
def servers(*args):
    for server in args:
        print(f"Server name: {server}")

servers("Server1", "Server2", "Server3", "Server4")
print()

def server_config(**kwargs): # keyword arguments - arguments are passed in as key=value pairs essentially
    print(kwargs)

server_config(
    server_name="Web-01",
    ip_address="192.68.0.120",
    region="us-east1",
    instance="t2.micro",
    infra="terraform"
)
print()

# with *args and **kwargs you can set up your function to take any number of parameters and key=value pairs
# which is useful for something like scripting for various servers and their respective configurations
def deploy2(env, *servers, **configs):
    print("Environment: ", env)
    print("Servers: ", servers)
    print("Configuration: ", configs)

deploy2(
    "prod",
    "db01",
    "db02",
    "db03",
    region="us.east1",
    instance="t3.medium",
    infra="terraform"
)
print()

## What is the difference between return and print ?
# print will output your result to the console, and does not send back whatever value to the calling function
# whereas return can send back the value to the calling function, and also can be used to exit out of a function early
def add(a, b):
    return a+b

print("Add with return")
result = add(10, 20) # return sends the value back to the caller of the function
print(result) # print will just display the value on the console
print(add(10, 20))

def print_add(a, b):
    print(a+b)

print("Add with print")
result = print_add(10,20) # since there is no return here result get sets to None
print(result)
print()

## Built-in functions for python

print(len("carla")) # finding the length of something
print(max(10,30)) # find the max between two numbers
print(sum([4,5,6])) # get the sum of the provided values

print()

## User-defined functions
# meaning you (the user) are defining the functions (isn't that basically the majority of them?)
def check_cpu(cpu):
    if (cpu > 80):
        return "High CPU usage"
    return "CPU usage normal"

print(check_cpu(92))
print(check_cpu(76))

print()

## Lambda function
# basically to write a function in a single line
# syntax:
#   lambda arguments: expression
#   - arguments: whatever values to perform the expression
#   - expression: the operation to perform on the arguments
# the output of the expression is automatically returned

def add(a, b):
    return a+b
print(add(10, 20))

add = lambda a, b: a+b
print(add(20,30))

square = lambda a: a*a
print(square(4))

print()

## Recursive functions
# a function that calls itself to resolve a problem

def count_down(n):
    if (n == 0):
        return
    
    print(n)
    count_down(n-1)

count_down(10)
print()

## Generator/generative function
# generally used to provide/produce certain values without fully stopping execute of the function
def numbers():
    yield 1
    yield 2
    yield 3

for number in numbers():
    print(number)


## Modules
# a collection of files which have functions that perform certain tasks, which you can import
# into your programs to reuse the existing functionality

# module
import math

result1 = math.pow(2, 3)
result2 = math.log(27)

print(result1)
print(result2)

import Calculator

result3 = Calculator.Add(10,20)
result4 = Calculator.Multiply(10, 2)

print(result3)
print(result4)
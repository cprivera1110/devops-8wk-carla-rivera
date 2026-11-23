## Type conversion / Casting
## Take input from the user age as integer and marks as string
## Convert marks and output the total sum
age = int(input("Enter your age: "))
marks = input("Enter your marks: ")

sum = age + int(marks)
print("Sum of age + marks = ", sum)
print()

## Sum program
## Take N numbers from the user and print the total sum
nums = int(input("Enter N numbers to sum: "))
sum = 0
for i in range(nums):
    sum += int(input("Enter number to add: "))
print(f"Sum of {nums} numbers = {sum}")
print()

## String methods
## Take a string input from the user and perform the following operations
## - print the string in uppercase and lowercase
## - print the total number of characters in the string
## - print the number of vowels in the string
str = input("Enter a string to manipulate: ")
print()
print("Uppercase : ", str.upper())
print("Lowercase : ", str.lower())
print("Total characters : ", len(str))
vowels = "aeiou"
vowel_count = 0
for vowel in vowels:
    vowel_count += str.lower().count(vowel)
print("Vowel count : ", vowel_count)
print()

## Keywords
## Write a program to check whether a given word is a Python keyword or not
keywords = "True, False, None, and, or, not, is, in, if, elif, else, for, while, break, continue, pass, def, return, lambda, yield, class, global, nonlocal, import, from, as, try, except, finally, raise, assert, async, await, with, del"
keep_going = True
while(keep_going):
    word = input("Enter your potential keyword: ")
    if (keywords.find(word) > 0):
        print("Python Keyword")
    else:
        print("Not a Keyword")
    answer = input("Would you like to try another? [y/n]: ")
    keep_going = answer == 'y'
print()

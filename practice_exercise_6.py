import math

# Check if a number is odd or even
def check_odd_even(num):
    if (num % 2 == 0):
        print("Even\n")
    else:
        print("Odd\n")

def get_number():
    while(True):
        try:
            num = int(input(f"Enter a number: "))
            break
        except:
            print("\tPlease enter a valid number!")
            continue
    return num

# Count the number of vowels in a string
def count_vowels(phrase=""):
    vowels = "aeiou"
    vowel_count = 0
    for vowel in vowels:
        vowel_count += phrase.lower().count(vowel)
    print("Total vowels: ", vowel_count)
    print()

# Check if a given number is prime
def check_prime(num):
    end = int(math.sqrt(num)+1)
    for i in range(2, end):
        if (num % i == 0):
            print("Not Prime\n")
            return
    print("Prime\n")

# Calculate the average of marks passed in a list
def average_marks(marks=[]):
    sum = 0
    for grade in marks:
        sum += grade
    avg = sum / len(marks)
    print("Average: ", avg)

def get_grades():
    print("Please enter your grades separated by a comma only.")
    grades = input("Enter your grades: ")
    marks = []
    for grade in grades.split(","):
        marks.append(int(grade))
    return marks

## Create and print a menu to select the tasks from.
def print_menu():
    print("--- Tasks Menu ---")
    print("1 - Check if a number is odd or even")
    print("2 - Count the number of vowels in a string")
    print("3 - Check if a number is prime or not")
    print("4 - Calculate the average for grades")

def get_task():
    while(True):
        try:
            task = int(input("Select an option (1-4) to perform the given task: "))
            if (task >= 1 and task <= 4):
                break
            else:
                print("Please enter a valid task number (1-4)!")
        except:
            print("Please enter a valid task number (1-4) only!")
            continue
    return task

keep_going = True
while(keep_going):
    print_menu()
    task = get_task()
    match task:
        case 1:
            num = get_number()
            check_odd_even(num)
        case 2:
            phrase = input("Enter a string to count the vowels: ")
            count_vowels(phrase)
        case 3:
            num = get_number()
            check_prime(num)
        case 4:
            marks = get_grades()
            average_marks(marks)
    cont = input("Would you like to perform another task? [y/N] ")
    keep_going = cont == 'y'
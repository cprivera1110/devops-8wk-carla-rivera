def print_odd_20():
    # range is 1 to 20 but for exclusive we go up to 21
    for i in range(1,21):
        if(i % 2 == 1):
            print(i, end=" ")
    print()

def print_57_mult_table():
    # range is 1 to 10 but for exclusive we go up to 11
    for i in range(1,11):
        print(f"57 x {i} = {57 * i}")

def print_multiples_3():
    for i in range(3,50,3):
        if(i != 15):
            print(i, end=" ")
    print()

def print_lowest_multiple(a, b):
    for i in range(1,1001):
        if (i % a == 0 and i % b == 0):
            print(i)
            break

def get_number(order):
    while(True):
        try:
            num = int(input(f"Enter {order} number: "))
            if (num > -1):
                break
            else:
                print("\tPlease enter a positive integer!")
        except:
            print("\tPlease enter a positive integer!")
            continue
    return num

def print_menu():
    print("--- Tasks Menu ---")
    print("1 - Print all odd numbers from 1 to 20")
    print("2 - Print the table of 57")
    print("3 - Print all multiples of 3 from 1 to 50 but skip 15")
    print("4 - Find lowest common multiple")

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

## Run a loop to perform these tasks from the given menu until the user would like to stop
keep_going = True
while(keep_going):
    print_menu()
    task = get_task()
    match task:
        case 1:
            print_odd_20()
        case 2:
            print_57_mult_table()
        case 3:
            print_multiples_3()
        case 4:
            a = get_number('first')
            b = get_number('second')
            print_lowest_multiple(a, b)
    cont = input("Would you like to perform another task? [y/N] ")
    keep_going = cont == 'y'
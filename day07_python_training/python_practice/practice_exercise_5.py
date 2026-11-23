## Unique roll numbers
roll_numbers = [101, 105, 102, 101, 108, 105, 110]
unique_roll_numbers = set(roll_numbers)
print(unique_roll_numbers)
print()

## Employee record search
employees = [(101, "Zola", 50000),
             (102, "Carla", 65000),
             (103, "Patrick", 45000),
             (104, "Joban", 55000),
             (105, "Calvin", 60000),
             (106, "Lawrence", 50000),
             (107, "Haiman", 45000)]

def get_id():
    while(True):
        try:
            num = int(input("Enter an employee id: "))
            if (num > -1):
                break
            else:
                print("\tPlease enter a valid id (positive integer) only!")
        except:
            print("\tPlease enter a valid id (positive integer) only!")
            continue
    return num

keep_going = True
while(keep_going):
    print("Welcome! Look up employee information by entering an employee ID.\nIf the employee exists, their information will be posted.")
    id = get_id()
    employee = [tup for tup in employees if id in tup]
    if (employee):
        print(f"Employee ID   : {employee[0][0]}")
        print(f"Employee Name : {employee[0][1]}")
        print(f"Salary        : {employee[0][2]}")
    else:
        print("Employee not found.")
    cont = input("Would you like to search for another employee? [y/N] ")
    keep_going = cont == 'y'
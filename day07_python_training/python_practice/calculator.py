def addition(a, b):
    try:
        result = a + b
    except:
        print("Invalid operation!")
        return
    return result

def subtraction(a, b):
    try:
        result = a - b
    except:
        print("Invalid operation!")
        return
    return result

def multiplication(a, b):
    try:
        result = a * b
    except:
        print("Invalid operation!")
        return
    return result

def division(a, b):
    try:
        result = a / b
    except:
        print("Invalid operation!")
        return
    return result

def remainder(a, b):
    try:
        result = a % b
    except:
        print("Invalid operation!")
        return
    return result

def power(a, b):
    try:
        result = a ** b
    except:
        print("Invalid operation!")
        return
    return result

def get_number(order):
    while(True):
        try:
            num = int(input(f"Enter {order} number: "))
            break
        except:
            print("Please enter a valid number!")
            continue
    return num

def get_operation():
    ops = "+, -, /, *, %, **"
    while(True):
        op = input("Choose operation (+, -, /, *, %, **): ")
        if (not ops.find(op) > -1):
            print("Please select a valid operation!")
            continue
        break
    return op

quit = False
while(not quit):
    a = get_number("first")
    b = get_number("second")
    op = get_operation()

    match op:
        case '+':
            result = addition(a, b)
        case '-':
            result = subtraction(a, b)
        case '/':
            result = division(a, b)
        case '*':
            result = multiplication(a, b)
        case '%':
            result = remainder(a, b)
        case '**':
            result = power(a, b)

    if (not type(result) == int):
        print("Sorry, that was an invalid operation!")
    else:
        print(f"Result: {a} {op} {b} = {result}")
    cont = input("Would you like to quit? [q to quit, anything else to continue] ")
    quit = cont == 'q'

def calculator():
    result = int(input("Enter your first number:"))
    while True:
        fun = input("Enter the function:")
        if fun == '+':
            num1 = int(input("Enter the number:"))
            result += num1
            print(int(result))
        elif fun == '*':
            num1 = int(input("Enter the number:"))
            result *= num1
            print(int(result))
        elif fun == '/':
            num1 = int(input("Enter the number:"))
            result /= num1
            print(float(result))
        elif fun == '-':
            num1 = int(input("Enter the number:"))
            result -= num1
            print(int(result))
        elif fun == '=':
            print("Result:", int(result))
            print("OFF")
            break
            
        else:
            print("!!!!!!!!!!!!!!!!!!!!Wrong input!!!!!!!!!!!!!!!!!!!!")
            continue
calculator()
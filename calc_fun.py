# Normal Calculator using Function
while True:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    print("""
Press + for Addition
Press - for subtraction
Press * for Multiplication
Press / for Division
""")

    choice = input("Enter the operator: ")


    def calc(digit1, digit2, operator):
        if operator == "+":
            result = digit1 + digit2
            return f"The Sum is {result}"
        elif operator == "-":
            result = digit1 - digit2
            return f"The Difference is {result}"
        elif operator == "*":
            result = digit1 * digit2
            return f"The Product is {result}"
        elif operator == "/":
            result = digit1 // digit2
            return f"The Division is {result}"
        else:
            result = "Enter correct choice "
            return result


    print(calc(num1, num2, choice))

    again = input("Press 'Y' to Continue"
                  "Press 'Q' to Quit").lower()
    if again == 'y':
        continue
    else:
        print("QUITING....THANKS FOR LETTING US SERVE YOU!!!!")
        break


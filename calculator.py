# Normal Calculator

print('''Hello User
This is a virtual calculator''')
while True:
    print('''
Press 1 for Addition
Press 2 for Subtraction
Press 3 for Multiplication
Press 4 for Division
Press 5 to Exit''')
    choice = int(input("Enter your choice "))
    if choice == 5:
        print("Quiting....")
        break
    num1 = int(input("Enter the first number "))
    num2 = int(input("Enter the second number "))
    if choice == 1:
        print('The Result is: ', num1+num2)
    elif choice == 2:
        print('The Result is: ', num1-num2)
    elif choice == 3:
        print('The Result is: ', num1*num2)
    elif choice == 4:
        print('The Result is: ', num1/num2)
    elif choice == 5:
        print("Quiting....")
        break
    else:
        print('Enter correct choice ')
"""i = 1
num = int(input(print("enter")))
while i <= 10:
    print(num, "*", i, "= ", pow(num, i))
    i += 1"""



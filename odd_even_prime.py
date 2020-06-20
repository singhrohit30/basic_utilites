# print("press n to Quit")
while True:
    num = int(input("Enter: "))
    if num % 2 == 0:
        print("Even")
        p = all((num % numbers != 0) for numbers in range(2, num))
        if p:
            print("Prime")
        else:
            print("Not Prime")

    else:
        print("Odd")
        p = all((num % numbers != 0) for numbers in range(2, num))
        if p:
            print("Prime")
        else:
            print("Not Prime")
    if num == 1:
        print("Prime")

    choice = input("Do you want to continue: ").lower()
    if choice == "y":
        continue
    elif choice == "n":
        print("quiting....")
        break
    else:
        print("Enter the correct choice:")
        choice = input("Do you want to continue:(y/n) ").lower()


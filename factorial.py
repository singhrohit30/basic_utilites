# factorial using while loop

while True:
    try:
        num = int(input("Enter: "))
    except Exception as e:
        print('Invalid Input!!', e)
    else:
        fact = 1
        while num > 0:
            fact = fact * num
            num -= 1
        print("The Factorial is: ", fact)
        exit()

# factorial using for loop

# while True:
#     fact = 1
#     num = int(input("Enter: "))
#     for number in range(1, num + 1):
#         fact = fact * number
#     print(fact)
#     choice = input("Press Y to continue? ").lower()
#     if choice == "y":
#         continue
#     else:
#         break

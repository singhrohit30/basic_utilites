first_num = 0
second_num = 1
third_num = 0
try:
    num_range = int(input("Enter the range: "))
except Exception as e:
    print("Invalid Input!!!", e)
else:
    print(first_num)
    print(second_num)
    for x in range(2, num_range):
        third_num = first_num + second_num
        print(third_num)
        first_num = second_num
        second_num = third_num


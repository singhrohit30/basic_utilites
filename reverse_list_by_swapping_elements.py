# reversing a list by swapping without using inbuilt function or Slicing

number_of_items = int(input('Enter the size of List: '))
sample_list = []
for i in range(number_of_items):    # Appending elements to the list/Creating the List
    sample_list.append(int(input(f'Enter item no. {i + 1}: ')))

for i in range(int((len(sample_list)) / 2)):  # len(sample_list) // 2 can also be used
    # Swapping the first nd last elements and iterating/traversing through the list simultaneously
    sample_list[i], sample_list[(len(sample_list) - 1) - i] = sample_list[(len(sample_list) - 1) - i], sample_list[i]

print('Reversed list is', sample_list)

# Python3 code to demonstrate
# each occurrence frequency using
# naive method

# initializing string
given_str = input("Enter the String: ")

# using naive method to get count
# of each element in string
character_frequency = {}

for i in given_str:
    if i in character_frequency:
        character_frequency[i] += 1
    else:
        character_frequency[i] = 1

# printing result
print("Count of all characters in String is :\n "
      + str(character_frequency))

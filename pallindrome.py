# TAKING INPUT FROM THE USER 'A WORD OR NUMBER'

word_or_number = input("Enter the Word or Number to which is to be checked: ")

# REVERSING THE GIVEN INPUT AND STORING IN A VARIABLE
 
is_pallindrome = word_or_number[::-1]

# CHECKING IF THE REVERSED IS EQUAL TO THE GIVEN INPUT

if is_pallindrome == word_or_number:
    print('PALLINDROME!')

else:
    print('NOT PALLINDROME!')
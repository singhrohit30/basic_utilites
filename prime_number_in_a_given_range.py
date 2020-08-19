# PROGRAM TO FIND PRIME NUMBERS IN A GIVEN RANGE

lower_limit, upper_limit = map(int, input('Enter the range (separated by a space): ').split())
prime_numbers = []
if upper_limit == 1:
    print(f'Prime number between {lower_limit}-{upper_limit}= 1')

else:

    for i in range(lower_limit, upper_limit + 1):  # to include the upper_limit '+1' is done
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)

print(f'Prime number between {lower_limit} and {upper_limit} =', prime_numbers)

# SECOND METHOD USING INBUILT 'all()' FUNCTION

'''
lower_limit, upper_limit = map(int, input('Enter the range (separated by a space): ').split())

prime_numbers = []

if upper_limit == 1:

    print(f'Prime number between {lower_limit} and {upper_limit}= 1')

else:

    for i in range(lower_limit, upper_limit + 1):
        result = all(i % j != 0 for j in range(2, i))
        if result:
            prime_numbers.append(i)

print(f'Prime number between {lower_limit} and {upper_limit} =', prime_numbers)

'''

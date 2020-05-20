# Raise a Number to a desired Power
from math import pow


def power(digit, strength):
    result = pow(digit, strength)
    return f"The number {digit} when raised to Power {strength} will result: {result}"


num = int(input("Enter: "))
unit = int(input("Enter the power to be raised: "))
print(power(num, unit))

# Question 2: Finding the range from a list of values without using built in functions
import sys
numbers = []
size = int(input("Enter the size of the list: "))
if size < 3:
    sys.exit("Range determination not possible")
else:
    # ask user to enter the elements of the list
    for _ in range(size):
        number = int(input("Enter a number: "))
        numbers.append(number)
    min = numbers[0]
    max = numbers[0]
    for number in numbers:
        if number >= max:
            max = number
        if number <= min:
            min = number
    print(f"Range:{max-min}")
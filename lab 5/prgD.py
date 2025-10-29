# Program to find 4-digit numbers in a given range
# that have all even digits and are perfect squares.
# Take the starting range (4-digit minimum) from the user
start_range = int(input("Enter the starting range (4 digit min): "))
# Take the ending range (4-digit maximum) from the user
end_range = int(input("Enter the ending range (4 digit max): "))# Create an empty list to store valid numbers
evendigit = []
# Loop through all numbers in the given range
for num in range(start_range, end_range + 1):
# Check if all digits in the number are even
# str(num) converts number to string so we can check each digit
# int(digit) % 2 == 0 → True if the digit is even
# all() returns True only if every digit passes the test
    if all(int(digit) % 2 == 0 for digit in str(num)):
# Calculate the square root of the number
       sqrt = int(num ** 0.5)
# Check if the number is a perfect square
       if sqrt * sqrt == num:
# Add the number to the list if it satisfies both conditions
           evendigit.append(num)
# After checking all numbers, print the result
if evendigit != []:
    print("Numbers with all even digits and are perfect squares:")
    print(evendigit)
else:
    print("There are no numbers within the given range.")
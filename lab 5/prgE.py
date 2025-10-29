# Program to generate all factors of a given number using while loop
# Take input from user
num = int(input("Enter a number: "))
# Initialize a variable to check divisors starting from 1
i = 1
# Print heading
print(f"Factors of {num} are:")
# Loop from 1 to num using while loop
while i <= num:
# If i divides num completely, it is a factor
    if num % i == 0:
        print(i, end=" ") # Print the factor on the same line
    i += 1 # Move to the next number
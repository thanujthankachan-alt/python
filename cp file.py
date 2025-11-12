# Write content to file3.txt
file = open("file3.txt", "w")
file.write("This is the first line\nThis is the second line\n This is the third line\n This is the fourth line\n")
file.close()

# Read first three lines
file = open("file3.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

# Copy only odd-numbered lines to file4.txt
file1 = open("file3.txt", "r")
file2 = open("file4.txt", "w")

line_number = 1
for line in file1:
    if line_number % 2 != 0:
        file2.write(line)
    line_number += 1

file1.close()
file2.close()

print("Odd lines written to file4.txt:")

# Display contents of file4.txt
file2 = open("file4.txt", "r")
for line in file2:
    print(line.strip())
file2.close()

file = open("file2.txt","w")
file.write("Hello World!\n welcome to python programing \n Thank you")
file.close()
list = []
file = open("file2.txt","r")
line = [line.strip() for line in file]
file.close()
print(line)
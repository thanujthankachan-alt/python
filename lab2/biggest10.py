s1 =int(input("enter num1 "))
s2 =int(input("enter num2 "))
s3 =int(input("enter num3 "))

if s1>s2 and s1>s3:
    l =s1
elif s2>s1 and s2>s3:
    l=s2
else:l=s3
print(l)

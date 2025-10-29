nums = input("Enter a list of intigers seperated by spaces: ").split()
result=[]
for n in nums:
    n=int(n)
    if n >100:
        result.append("over")
    else:
        result.append(n)
        print(result)
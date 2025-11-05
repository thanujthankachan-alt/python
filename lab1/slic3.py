user_input=input("enter a string:")

if user_input:
    first_char=user_input[0]
    modified_string=first_char+user_input[1:].replace(first_char,"$")
    print("modified_string:",modified_string)
else:
    print("please entered an empty string.")


user_string = input("Enter a string: ")
string_length = len(user_string)
i = string_length - 1

if string_length == 0:
    print("Something went wrong or you did not enter an input!")
    print("Please try entering a string!")

while i > 0 :
    if user_string[i] == "a" or user_string[i] == "b":
        i = i - 1
    else:
        print("String contains letters other than 'a' and 'b' ")
        i = -5
        
if i != -5:
    print("The string is made only of 'a' and 'b'")
"""Q7: Input a string and check if it is palindrome or not?"""

data = input("enter the string : ")
new_Data = data[::-1]
if data==new_Data:
    print("pallindrom")
else:
    print("not a palindrom")
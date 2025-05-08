'''
Write a program to calculate whether character is in lowercase
or uppercase.
'''

x = input()
ascii_value = ord(x)

if (ascii_value > 91 ) :
    print(x , "Is a LowerCase")
else :
    print(x ,'Is UpperCase ')
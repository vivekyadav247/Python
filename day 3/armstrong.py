'''
Write a program that accepts a three digit number from user
and check whether it is Armstrong or not.(eg.153= 1 3 +5 3 +3 3 )
'''

x = input()

s = int(x[0])**3
s += int(x[1])**3
s += int(x[2])**3

if int(x) == s :
    print(s ,"This is Armstrong number ")
else :
    print( s ,"This is not Armstrong number ")
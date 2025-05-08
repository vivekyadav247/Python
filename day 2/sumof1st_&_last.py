'''Write a program that accepts four digit number from user and
calculate the sum of first and last digit.'''

x = input ()
print(x)
sum = int (x[0]) + int (x[-1])
print(sum)
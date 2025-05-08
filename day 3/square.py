'''
Write a program to calculate sum of squares of n natural
number.
'''
n = int(input())
sum = 0
for i in range (0, n+1) :
    sqr = i**2
    sum += sqr
    print(sum)
    n -= 1
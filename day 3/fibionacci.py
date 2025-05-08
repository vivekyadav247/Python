'''
Write a program to print Fibonacci Series.
'''
x = int(input())
last = 0
curr = 1
print(last,curr,end=" ")
for i in range (3,x+1) :
    sum =curr+last
    print(sum,end=" ")
    last = curr
    curr = sum 

'''
Write a program to calculate Factorial of any number.
'''
x = int(input())
fact = 1
for i in range (1,x+1) :
    fact *= x
    x -= 1
    if x == 0:
        break
print(fact)
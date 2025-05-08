'''
Write a program to calculate largest number out of given four
numbers.
'''

x = input()

if (x[0] > x[1] and x[0] > x[-1] and x[0] > x[2]) :
    print(x[0] ,' is gratest element ')
elif (x[1] > x[0] and x[1] > x[-1] and x[1] > x[2]) :
    print(x[1] ,' is gratest element ')
elif (x[2] > x[0] and x[2] > x[-1] and x[2] > x[1]) :
    print(x[2] ,' is gratest element ')
else :
    print(x[-1], ' is greatest element ')
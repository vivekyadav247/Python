'''
Write a program that accepts marks (out of 100) of five subjects
percentage? Display message according to following condition
percentage &gt;=60 Grade A
percentage &gt;=50 Grade B
percentage &gt;=40 Grade C
percentage &lt;40 Grade D
'''


marks = int(input())

if marks >= 60 :
    print('A Grade')
elif marks >= 50 and marks < 60 :
    print('B Grade')
elif marks >= 40 and marks <50 :
    print('C Grade')
else :
    print('D Grade')
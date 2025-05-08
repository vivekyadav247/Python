'''Write a program that accepts marks of five subjects
subject from user and calculate the total marks and then calculate
the percentage out of 500?'''

marks = []
sum = 0
for i in range (0,5):
    marks.append(int(input(f"Enter {i+1} subject marks : ")))
    sum += marks[i]
print()
print(marks)
print('Total marks out of 500 are : ',sum)
print()
p = (sum / 500 )*100
print("Percentage is : ", p)


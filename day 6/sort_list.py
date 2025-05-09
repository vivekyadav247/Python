'''Q7: WAP to sort elements of 8 element list in descending order ,
without using builtin method?'''
list=[]
for i in range (8) :
    list.insert(i,input())
print(list)
for i in range (8) :
    for j in range (i+1,8,1) :
        if list[i] < list[j] :
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

print(list)
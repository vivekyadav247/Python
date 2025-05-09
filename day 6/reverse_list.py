list = [1,2,3,4,5,6]
print(list)
i = 0 
j = len(list)-1

while i < j :
    if list[i] < list[j] :
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
    i+=1
    j-=1

print(list)


'''Q9: WAP to search element inside list?'''
list = [1,2,3,4,5,6]
print(list)
target = int(input("Enter target to search : "))
i = 0 
j = len(list)-1
while i<=j :
    k = int((i+j)/2 )
    if list[k]==target :
        print("Target is found at",i,"th index")
        break 
    elif list[k]>target :
        j = k-1
    else : i = k+1

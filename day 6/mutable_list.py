'''Q4: WAP to justify list is mutable in nature?'''
list = [1,2,3,4,5,6]
print(list)
list.insert(1,9)
print(list)
list.append(10)
print(list)
list.remove(1)
print(list)
list.pop()
print(list)
print("Here we can edit list from everywhere , then we can say list is mutable")


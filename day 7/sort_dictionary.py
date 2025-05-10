"""Q4: Write a Python script to sort (ascending and descending) a
dictionary by value."""


dict1={"a":1,"c":3,"d":2,"e":7,"f":6}
key = []
val=[]
for k,v in dict1.items():
    key.append(k)
    val.append(v)
print(key)
print(val)
dict2={}
for i in range(len(val)):
    for j in range(len(val)-1):
        if val[j]<val[j+1]:
            val[j],val[j+1]=val[j+1],val[j]
            key[j],key[j+1]=key[j+1],key[j]
for i in range(len(val)):
    dict2.update({key[i]:val[i]})
print(dict2)


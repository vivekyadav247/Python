'''Q2: WAP to create dictionary containing user details , access each
details manually using keys &amp; via loop?'''


n = int(input("Enter the length of dictionary : "))
x={}
for i in range (n) :
    key = input(f"Enter {i+1} key : ")
    value = int(input(f"Enter value of {i+1} key : "))
    x[key] = value 

print(x)
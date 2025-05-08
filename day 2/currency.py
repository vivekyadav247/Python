x = int(input("Enter a Amount : "))
count = 0
while (x > 0) : 
    if x >= 1000 :
        count = x // 1000
        x =  x%1000
    elif x>=500 :
        count += x // 500
        x = x%500
    elif x >=100 :
        count += x//100
        x = x%100
    elif x>=50 :
        count += x//50 
        x = x%50
    elif x >= 10 :
        count += x//10
        x = x%10
    elif x >= 5 :
        count += x//5
        x = x%5
    else :
        count += 1
        x -= 1
print("Minimum No. of Note and Coin to fulfill this amount : ",count)
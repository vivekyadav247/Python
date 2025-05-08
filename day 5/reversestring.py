X=str(input("Enter Your String: "))

def reverse():
    Y=""
    for i in range (-1,-len(X)-1,-1):
        Y+=X[i]
    print(Y)
reverse()
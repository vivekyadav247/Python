def perfect(n):
    sum =0
    for i in range (1,n):
        if n%i == 0:
            print(i)
            sum +=i
    if sum == n:
        print("Number is perfect")
    else:
        print("Number is not perfect")

n = int(input("Enter the Number :"))
perfect(n)
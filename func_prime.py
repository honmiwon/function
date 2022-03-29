def num():
    a=int(input("enter the number:"))
    i=1
    j=0
    while i<=a:
        if a%i==0 and a%a==0:
            j=j+1
        i=i+1
    if j==2:
        print("it is a prime")
    else:
        print("it is not a prime") 
num()                   
# list=[55,23,00]
# i=0
# sum=""
# while i<=len(list):
#     sum=sum+str(list[i])
#     i+=1
# print(sum)
 
def func(x):
    i=0
    sum=''
    while i<len(x):
        sum=sum+str(x[i])
        i=i+1
    return sum
print(func([55,23,10]))       
def check_numbers(num,num2):
    if num%2==0 and num2%2==0:
        print("both are even")
    else:
        print("both are not even")
check_numbers(4,66)
def check_numbers_list(list1,list2):
    i=0
    while i<len(list1) and i<len(list2):
        if list1[i]%2==0 and list2[i]%2==0:
            print("both are even numbers")
        else:
            print("both are not even numbers")
        i+=1
check_numbers_list([12,6,18,10,3,75],[6,19,24,12,3,87])                                   
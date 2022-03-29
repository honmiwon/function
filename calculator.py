def calculator(number_x,number_y,operator):
    if operator=="add":
        sum=number_x+number_y
        print(sum)
    elif operator=="sub":
        sub=number_x-number_y
        print(sub) 
    elif operator=="multiply":
        mul=number_x*number_y
        print(mul)
    else:
        div=number_x%number_y
        print(div)
calculator(20,25,"add")
calculator(40,3,"sub") 
calculator(10,4,"multiply") 
calculator(40,4,"div")                 
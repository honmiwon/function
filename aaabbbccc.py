def function(A):
    i=0
    x=""
    while i<len(A):
        if A[i] != A[i-1]:
            x+=A[i]
        i +=1
    print(x) 
function(["a","a","a","b","b","b","c","c",""])           
                
# given integers from 1 to N
# and an array with numbers 1 to N,  only one number repeated, one missing 
from functools import reduce


def missingAndRepeating(arr, n):
    # Write your code here
    gp = reduce(lambda x,y: x*y, [i for i in range(1,n+1)])
    ap = int(n*(n+1)/2)
    
    sum_arr = sum(arr)
    mul_arr = reduce(lambda x,y: x*y, arr)
    print(gp, ap, sum_arr, mul_arr)
    
    rep = round((sum_arr - ap) / (1-(gp/mul_arr)))
    
    missing = int(ap + rep - sum_arr)
    
    return missing, rep 


print(missingAndRepeating([7, 5, 3, 2, 1, 6,6], 7))
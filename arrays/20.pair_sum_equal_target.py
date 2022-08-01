# Given an array, find pairs whose sum is equal to given number

from math import factorial

def pairSum(arr, s):
    # Write your code here.
    lst = []
    
    dct = {}
    for i in arr:
        dct[i] = dct.get(i, 0) + 1
    
    for key in dct:
        key1 = s - key
        if key1 in dct and dct[key]>0 and dct[key1]>0:

            # this is important cause if the example shown below we wil have all the 2s in one key
            # hence we need see in how many ways we can find pairs from them
            # here eg: dct[2]=3,  hence  3c2 ways 
            # else you can just multiply key and key1 values 
            if key1==key:
                tot = int(factorial(dct[key]) / (2*(factorial(dct[key]-2))))
            else:
                tot = dct[key] * dct[key1]

            for i in range(tot):
                lst.append([key, key1])
            dct[key] = 0
            dct[key1] = 0

    print(lst)


pairSum([2, -3, 3, 3, -2], 0)
pairSum([2, -6, 2, 5, 2], 4)
    
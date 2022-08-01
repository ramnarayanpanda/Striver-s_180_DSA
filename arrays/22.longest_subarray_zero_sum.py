def LongestSubsetWithZeroSum(arr):
    prefix_sum = [arr[0]]
    sm = arr[0]
    
    for i in arr:
        sm += i
        prefix_sum.append(sm)
    
    dct = {}
    maax = 0
    for i, key in enumerate(prefix_sum):
        if key in dct:
            maax = max(maax, i-dct[key])
        else:
            dct[key] = i
            
    return maax


print(LongestSubsetWithZeroSum([1, 2, 1, -2]))
print(LongestSubsetWithZeroSum([1, 2, 3, 4, -7, 2, 9, -9]))



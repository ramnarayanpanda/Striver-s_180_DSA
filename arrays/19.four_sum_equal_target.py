def fourSum(arr, target):
    # Write your code here
    dct = {}
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            key = arr[i]+arr[j]
            if key in dct:
                dct[key].append((i,j))
            else:
                dct[key] = [(i,j)]
    
    print(dct)
    for key in dct:
        key1 = target - key
        if key1 in dct:
            for i in dct[key]:
                for j in dct[key1]:
                    if (i[0]!=j[0]) and (i[1]!=j[0]) and\
                       (i[0]!=j[1]) and (i[1]!=j[1]):
                        return 'Yes'
    return 'No'



print(fourSum([2, 4, 6, 3, 1, 1], 20))
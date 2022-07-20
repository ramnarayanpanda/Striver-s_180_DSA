def nextPermutation(permutation, n):
    
    pos = float('inf')
    
    # first iterate through the array in reverse order to find the elem which is smaller than the next elem in array 
    # hence it means all the elems till this elem is in sorted order,  
    # eg:  [2, 3, 1, 5, 4]
    # then pos = 2,  cause lst[3] > lst[2]
    for i in range(n-2,-1,-1):
        if permutation[i+1] > permutation[i]:
            pos = i
            break
    
    # if the array is already sorted in reverse order than as per the question we just need to reverse the array and return
    if pos==float('inf'):
        return permutation[::-1]
    
    # else we need to traverse again from the end of the array to find the smallest element from the current element at pos 
    # then swap these 2 elems, so we got our pos elem set to the lexi order, 
    # now we know that the array is reverse sorted from pos to end, but we need to reverse it to get lexi order
    
    # eg:   [2, 3, 1, 5, 4],  pos=2 
    # pos1 = 4,  as  lst[4] > lst[2] 
    # swap(pos, pos1),  lst=[2,3,4,5,1],  here you can see that we got the elem that we need at pos(index 2)
    # after pos you can see that lst is sorted in reverse order, we just need to reverse it again  
    # lst = [2, 3, 4] + [5, 1][::-1] -->> [2, 3, 4, 1, 5]
    else:
        for i in range(n-1, pos, -1): 
            if permutation[i]>permutation[pos]:
                pos1 = i
                break

        print(pos, pos1) 
        permutation[pos], permutation[pos1] = permutation[pos1], permutation[pos]
        return permutation[:pos+1] + permutation[pos+1:][::-1]
    
    
    
# nextPermutation([2, 3, 1, 5, 4], 5)
# nextPermutation([2, 3, 1, 5, 4, 6, 8, 7, 7, 0], 10)
# nextPermutation([1, 2], 2)
# nextPermutation([1, 2, 3, 4, 5], 5)
# nextPermutation([1], 1)
# nextPermutation([4, 3, 2, 1], 4)
# nextPermutation([2, 1, 3, 4], 4)
print(nextPermutation([1, 3, 2], 3))
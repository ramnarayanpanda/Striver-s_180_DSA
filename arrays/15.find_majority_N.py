# this solution is basically the generalization form of what we solved in the previous one

# first while: will check if any elem in cnts is same as cur_elem
#              if it is same then it will increment the cnt for that elem
#              once the if statisfies we dont need to check it again, cause we incremented cnt of cur_elem
#              Also if we are incrementing then no need to go to the next statement, i.e.   if j==(k-1):

# if j==(k-1): This statifies when the cur_elem is not present in the nums, in this case the value of j=k-1 
#              Here we will again traverse through the cnts array and check if anyone elem in cnts array is 0,
#              then we will add the cur_elem in nums, and corresponding cnt will increase by 1
#              if none of the cnts is zero then we need to subtract one from every elem in the cnts array in the for loop ll


def repeatedNumber(A, k):
    n = len(A) 
    cnts = [0]*(k-1)
    nums = [-1]*(k-1)

    for i in range(n):
        j = 0

        while j<(k-1):
            if nums[j]==A[i]:
                cnts[j]+=1
                break 
            j+=1
        
        if j==(k-1):
            l = 0

            while l<(k-1):
                if cnts[l]==0:
                    cnts[l] = 1
                    nums[l] = A[i]
                    break 
                l += 1
            
            if l==(k-1):
                for ll in range(k-1):
                    cnts[ll] -= 1

    
    for i in nums:
        cnt = 0
        for j in A:
            if i==j:
                cnt += 1
        if cnt>(n/k):
            return i 
    
    return -1 


print(repeatedNumber([1, 2, 1, 5, 8, 8, 10, 1, 3, 1], 3))
print(repeatedNumber([1, 2, 1, 5, 8, 8, 10, 1, 3, 1, 3, 5], 3))

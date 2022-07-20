def maxSubarraySum(arr, n) :

	# Your code here
    cur_best, overall_best = arr[0], -float('inf')
    
    # if cur_elem is greater than cur_best + cur_elem then it is better that the cur_elem starts a new chain from itself
    # except this case for other cases you can add the cur_elem to cur_best even if the cur_elem makes the cur_best -ve 
    # cause whi knows may be after the cur_elem we will get a very big number that will even increase the cur_best 
    for i in range(1, n):
        if arr[i]>cur_best+arr[i]:
            cur_best = arr[i]
        else:
            cur_best = cur_best + arr[i]
        overall_best = max(overall_best, cur_best)
    
    return max(0, overall_best)


# maxSubarraySum([1, 2, 7, -4, 3, 2, -10, 9, 1], 9)
maxSubarraySum([10, 20, -30, 40, -50, 60], 6)
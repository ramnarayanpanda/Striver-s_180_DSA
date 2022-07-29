# find the elem which repeats more than N/2 times in an array 


def findMajorityElement(arr, n):
	# Write your code here.
	
    elem = arr[0]
    cnt = 1
    
    for i in arr:
        if i==elem:
            cnt+=1
        else:
            cnt-=1
            if cnt==0:
                elem = i
                cnt = 1
    
    return elem if  len([i for i in arr if i==elem]) > len(arr)/2 else -1


print(findMajorityElement([2, 3, 9, 2, 2, 4], 2))
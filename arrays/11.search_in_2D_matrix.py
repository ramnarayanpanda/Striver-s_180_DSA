# return true if a number present in an array, else return false 
# each row is sorted, and also the last elem of each row is greater than first elem of current row 


# order of solution =  log(m) + log(n)  =  log(m*n) 


# this function returns the index of the target element,
# if the target is not present then it will return the index of closest smallest integer 
def binary_search(arr, x):
    l = 0
    r = len(arr) - 1

    if arr[l] >= x:
        return l
    elif arr[r] <= x:
        return r
    
    while l < r-1:
        mid = (l + r) // 2

        if arr[mid] == x:
            return mid 
        elif arr[mid] < x:
            l = mid 
        else:
            r = mid 

    return l


def findTargetInMatrix(mat, m, n, target):
    
    # the idea here is to first find the row where the lement might be present 
    # then use that row to find the exact position of target, 
    # if the target is present then you will get the exact row and col index 
    # otherwise as mentioned in the above you will get the closest value's index
    # that is why we are agin checking arr[row][col]==target 
    lst = [row[0] for row in mat]
    
    row = binary_search(lst, target)
    
    col = binary_search(mat[row], target)
    
    if mat[row][col]==target:
        return True 
    else:
        return False
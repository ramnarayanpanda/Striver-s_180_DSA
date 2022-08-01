# return lenght of longest consecutive sequence 
# eg: [100, 200, 1, 3, 2, 4]  4 -> 1 2 3 4

# brute force: sort then check it will be   O(N*logN)

# optimized: put everythin into a set and till we get n+1 for a number run while 


def lengthOfLongestConsecutiveSequence(arr, n):
    s = set(arr) 
    length = 1

    for i in arr:
        cnt = 1
        while i+1 in s:
            i+=1
            cnt+=1
        length = max(length, cnt)
    
    return length 


print(lengthOfLongestConsecutiveSequence([33, 20, 34, 30, 35], 5))
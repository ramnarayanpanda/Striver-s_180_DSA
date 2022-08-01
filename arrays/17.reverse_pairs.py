# Given an array find all pairs such that  i<j  and  arr[i] > 2 * arr[j]



def reversePairs(arr):


    def merge(arr, l, m, r):
        nonlocal total_cnt 
        n1 = m - l + 1
        n2 = r - m
    
        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
    
        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]
    
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i, j = 0, 0
        while i<n1:
            if j<n2 and L[i] > 2*R[j]:
                while j<n2 and L[i] > 2*R[j]:
                    j+=1
            i+=1   
            total_cnt += j
    
        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

        print(arr, n1, n2, L, R, total_cnt) 


    def mergeSort(arr, l, r):
        if l < r:
            m = l+(r-l)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)

    total_cnt = 0
    _ = mergeSort(arr, 0, len(arr)-1)
    return total_cnt



print(reversePairs([2, 8, 7, 5, 3, 11, 6, 8, 14]))
# print(reversePairs([6, 4, 8, 2, 1, 3]))
# print(reversePairs([7, 9, 9, 3, 7, 4, 4, 3, 4, 4]))
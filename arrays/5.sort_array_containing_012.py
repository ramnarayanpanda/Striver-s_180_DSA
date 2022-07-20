# we have array of 0, 1, 2.  Sort the array by traversing JUST ONCE THROUGH the array
# do it inplace 


# this solution contains traversing thorugh the array TWICE  
def sort012(arr, n) :
    dct = {}
    for i in arr:
        dct[i] = dct.get(i, 0) + 1
        
    ind = 0
    for i in range(dct[0]):
        arr[ind] = 0
        ind+=1 
    for i in range(dct[1]):
        arr[ind] = 1
        ind+=1 
    for i in range(dct[2]):
        arr[ind] = 2
        ind+=1 
            
    return arr  



def sort012_1(arr, n):
    low, mid, high = 0, 0, n-1  
    
    while mid<high:
        if arr[mid]==0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low+=1 
            mid+=1      
        if arr[mid]==1:
            mid+=1  
        if arr[mid]==2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high-=1
    
    return arr 
        






            
arr = [0, 1, 2, 1, 2, 1, 2]
print(sort012(arr, len(arr)))  

arr = [2, 2, 2, 1, 1, 1, 0]
print(sort012(arr, len(arr)))  

arr = [0, 1, 2, 1, 2, 1, 2]
print(sort012_1(arr, len(arr)))  

arr = [2, 2, 2, 1, 1, 1, 0]
print(sort012_1(arr, len(arr)))  


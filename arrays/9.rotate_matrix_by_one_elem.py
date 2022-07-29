def rotate(mat):
    
    n = len(mat) 
    m = len(mat[0])
    
    cnt = 0
    while cnt<min(n//2, m//2):
        temp = mat[cnt][cnt] 
        
        row = cnt 
        col = cnt 
        
        while row<n-1-cnt:
            mat[row][col] = mat[row+1][col]
            row+=1
            
        while col<m-1-cnt:
            mat[row][col] = mat[row][col+1]
            col+=1 
            
        while row>cnt:
            mat[row][col] = mat[row-1][col]
            row-=1
            
        while col>cnt:
            mat[row][col] = mat[row][col-1]
            col-=1
        
        print(row, col+1)
        print(mat[row][col+1], temp)
        mat[row][col+1] = temp 
        cnt+=1
        
    return mat 


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 6
lst = [[(i*n)+j for j in range(1,1+n)] for i in range(n)]


lst = [[1, 2, 3, 4, 5, 6, 7, 8], 
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8]]


# for i in lst:
#     print(i)
# print()


lst = [[-3,  5,  3, -9, -2, 10,  3, 1], 
       [-6, -9, -9, -1, 10,  6, -7, 8]]


lst = [[5,    5,  -9,  3],  
       [3,   -5,  -5,  6], 
       [8,    5,  10, -10],  
       [9,   -5,  -4,   0], 
       [10,  -8,  -6,  -7], 
       [-10, -1,  -9,  -6], 
       [-6,   7,  -10,  4], 
       [4,   -2,   8,  -8]]




lst = rotate(lst)

print()
for i in lst:
    print(i)
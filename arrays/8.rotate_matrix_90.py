def rotate(matrix):
    n = len(matrix)
    
    for i in range(n//2 + n%2):
        for j in range(n//2):
            temp = matrix[i][j]
            
            matrix[i][j] = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
            matrix[j][n-i-1] = temp
                    
    return matrix


lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lst = [[(i*5)+j for j in range(1,6)] for i in range(5)]


for i in lst:
    print(i)

n = len(lst) 
m = len(lst[0])
lst = rotate(lst)
print('\n\n')
for i in lst:
    print(i)

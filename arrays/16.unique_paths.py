# find the number of unique paths in which you can travel from the [0][0] to [m-1][n-1] position of a matrix
# you can only travle either down or right 

# Here the idea is to fill the n-1 indexed column and m-1 indexed row with ones, 
# cause from them we can only travel in one direction / we will only have one path from them
# the other cells will add up to what we have in the row+1 and col+1 cells 
# cause we can travel from any current cell to the row+1 and col+1 cell


def uniquePaths(m, n):
	# Write your code here.
    mat = [[0 for i in range(n)] for j in range(m)]
    for row in range(m-1, m):
        for col in range(n):
            mat[row][col] = 1
            
    for col in range(n-1, n):
        for row in range(m):
            mat[row][col] = 1

    # print(mat)
            
    for row in range(m-2, -1, -1):
        for col in range(n-2, -1, -1):
            # print(row, col, mat[row][col-1] + mat[row-1][col])
            mat[row][col] = mat[row][col+1] + mat[row+1][col]
            
    # print(mat)
    return mat[0][0]


print(uniquePaths(3, 2))
print(uniquePaths(2, 2))
print(uniquePaths(1, 1))
print(uniquePaths(1, 6))
print(uniquePaths(4, 4))
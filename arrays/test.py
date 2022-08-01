L = [3, 7, 7, 9, 9] 
R = [3, 4, 4, 4, 4]

n1 = len(L)
n2 = len(R)
i, j = 0, 0

total_cnt = 0

while i<n1:
    if j<n2 and L[i] > 2*R[j]:
        while j<n2 and L[i] > 2*R[j]:
            j+=1
    i+=1   
    total_cnt += j


print(total_cnt)
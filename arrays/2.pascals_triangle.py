import math

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    lst = []
    
    row_cnt = 1
    
    while row_cnt<n+1:
        cur_elem = 0
        lst1 = []
        while cur_elem<math.ceil(row_cnt/2):
            if cur_elem==0:
                elem = 1 
            else:
                elem = lst[-1][cur_elem] + lst[-1][cur_elem-1]
            cur_elem += 1
            lst1.append(elem)
            
        if row_cnt%2==0:
            lst1 = lst1 + lst1[::-1]
        else:
            lst1 = lst1 + lst1[0:-1][::-1]
            
        lst.append(lst1)
        row_cnt+=1

    return lst 
            
            
            
            
            
            
            
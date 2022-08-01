# the idea here is simple, we just need to take 2 variables to store 2 numbers
# another 2 variables for the count of the numbers

# if num1==cur_elem, then increase cnt1 by 1
# if num2==cur_elem, then increase cnt2 by 1
# if any of the cnt is empty / 0, means it does not contain any element, 
#                                 then we can add the cur_elem to that num and make cnt to 1

# else if both the cnts are not 0, then we can do a -1 for both of them

def repeatedNumber(A):

    num1, num2 = -1, -1
    cnt1, cnt2 = 0, 0 

    for i in A:
        if num1==i:
            cnt1 += 1
        elif num2==i:
            cnt2 += 1
        elif cnt1==0:
            num1 = i
            cnt1 = 1
        elif cnt2==0:
            num2 = i
            cnt2 = 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    if len([i for i in A if i==num1])>len(A)/3:
        return num1 
    elif len([i for i in A if i==num2])>len(A)/3:
        return num2 
    else:
        return -1


print(repeatedNumber([1, 2, 1, 5, 8, 8, 10, 1, 3, 1]))
print(repeatedNumber([1, 2, 1, 5, 8, 8, 10, 1, 3, 1, 3, 5]))

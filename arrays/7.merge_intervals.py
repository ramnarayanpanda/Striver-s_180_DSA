def merge(intervals):
    intervals.sort()
    lst = [intervals[0]]

    for i in range(1, len(intervals)):
        intr1, intr2 = lst[-1], intervals[i]

        if intr2[1]<=intr1[1]:
            continue 
        elif intr2[0]<=intr1[1]:
            lst[-1] = [lst[-1][0], intr2[1]]
            continue 
        else:
            lst.append(intr2)
    return lst


print(merge([[1, 4], [3, 5], [6, 8], [10, 12], [8, 9]]))
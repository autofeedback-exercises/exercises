def separateEvenOdd(mylist):
    evenList, oddList = [], []
    for item in mylist:
        if (item % 2) == 0:
            evenList.append(item)
        else:
            oddList.append(item)
    return oddList, evenList


print(separateEvenOdd([1, 2, 3, -4, 5, 6, 7, 8, 9]))

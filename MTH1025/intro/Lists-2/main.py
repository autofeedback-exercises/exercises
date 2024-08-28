def separateEvenOdd(mylist):
    return [j for j in mylist if j%2 == 0], [j for j in mylist if j%2 != 0]

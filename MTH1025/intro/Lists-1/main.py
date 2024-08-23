def addToList(mylist, x):
    mylist.append(x)
    return mylist
def truncateList(mylist, N):
    if N > len(mylist):
        return mylist
    else:
        return mylist[:-N]
print(addToList([1,2,3], 4))
print(truncateList([1,2,3],1))
print(truncateList([1,2,3],4))

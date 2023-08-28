
def ispositive(x):
    if x > 0:
        return("positive")
    elif x<0:
        return("negative")
    else:
        return("zero")

print (ispositive(3))
print (ispositive(-3))
print (ispositive(0))

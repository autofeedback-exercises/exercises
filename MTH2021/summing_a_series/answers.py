# write your code here

def sum_geometric(x,N):
    S=0
    for n in range(N+1):
        S+=x**n
    return(S)

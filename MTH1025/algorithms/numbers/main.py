#NOTEBOOK numbers1.ipynb numbers2.ipynb
def numberOfThousands(N):
    from math import floor
    return floor(N/1000)

#NOTEBOOK numbers2.ipynb
from math import floor
def numberOfHundreds(N):
    return floor((N-1000*numberOfThousands(N))/100)
def numberOfTens(N):
    return  floor((N-(numberOfHundreds(N)*100+1000*numberOfThousands(N)))/10)
def numberOfOnes(N):
    return  floor((N-(100*numberOfHundreds(N)+1000*numberOfThousands(N)+10*numberOfTens(N))))
def decompose(N):
    return [numberOfThousands(N), numberOfHundreds(N), numberOfTens(N),
            numberOfOnes(N)]

#NOTEBOOK numbers3.ipynb
def decompose(N):
    from math import floor
    div = 1000
    number = []
    while div >= 1:
        digit = floor(N / div)
        N = N - div * digit
        div = div / 10
        number.append(digit)
    return number

#NOTEBOOK numbers4.ipynb
def decompose(N, digits=4, base=10):
    from math import floor
    div = base**(digits-1)
    number = []
    while div >= 1:
        digit = floor(N / div)
        N = N - div * digit
        div = div / base
        number.append(digit)
    return number

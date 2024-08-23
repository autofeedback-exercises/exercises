import matplotlib.pyplot as plt
import numpy as np
order = ['exponents', 'multiplication', 'addition']

q1 = (13 * 4 )** 2
q2 = 5 / 10
q3 = 10 / (2 + 3)
q4 = 6*3

a1=3
b2=(4+5)/2
c3=3*(9+4)
d4=(7+4)*(10/2)

numerator = (4+5)*(3+0.5)
denominator = 7*(10-4)
r = numerator/denominator
numerator=4

c3 = 4
e5 = c3 + 5
b2 = e5*c3
f6 = b2 + e5
d4 = c3 / f6
a1 = ( c3 + e5 ) / ( f6 + d4 )

table = 13
zeroTimes = 0*table
oneTimes = 1*table
twoTimes = 2*table
threeTimes = 3*table
fourTimes = 4*table
fiveTimes = 5*table
sixTimes = 6*table
sevenTimes = 7*table
eightTimes = 8*table
nineTimes = 9*table
tenTimes = 10*table
print(zeroTimes)
print(oneTimes)
print(twoTimes)
print(threeTimes)
print(fourTimes)
print(fiveTimes)
print(sixTimes)
print(sevenTimes)
print(eightTimes)
print(nineTimes)
print(tenTimes)

table = 7
timesTable = np.zeros(11)
timesTable[0] = 0*table
timesTable[1] = 1*table
timesTable[2] = 2*table
timesTable[3] = 3*table
timesTable[4] = 4*table
timesTable[5] = 5*table
timesTable[6] = 6*table
timesTable[7] = 7*table
timesTable[8] = 8*table
timesTable[9] = 9*table
timesTable[10] = 10*table
print( timesTable)

table = 7
timesTable = np.zeros(11)
timesTable[0] = 0*table
timesTable[1]  = 1*table
timesTable[2]  = 2*table
timesTable[3]  = 3*table
timesTable[4]  = 4*table
timesTable[5]  = 5*table
timesTable[6]  = 6*table
timesTable[7]  = 7*table
timesTable[8]  = 8*table
timesTable[9]  = 9*table
timesTable[10]  = 10*table
print(table)
#print(timesTable)
print(timesTable[0],timesTable[1],timesTable[2],timesTable[3],timesTable[4],timesTable[5],timesTable[6],timesTable[7],timesTable[8],timesTable[9],timesTable[10])


table = 7
timesTable = np.zeros(11)
for i in range(11) : timesTable[i] = i*table
print(timesTable)

table = 27
timesTable = np.zeros(16)
for i in range(16) : timesTable[i] = i*table
print(timesTable)

table = 7
xvals = np.zeros(11)
yvals = np.zeros(11)
for i in range(11) : 
    xvals[i] = i
    yvals[i] = i*table
plt.plot( xvals, yvals, 'ko' )
plt.xlabel('Index')
plt.ylabel('Seven times table')
# This code is required for the Automated feedback, don't delete it!
fighand = plt.gca()

plt.figure()
xvals = np.zeros(30)
yvals = np.zeros(30)
for i in range(30) : 
    xvals[i] = i
    yvals[i] = i*i
plt.plot( xvals, yvals, 'ko' )
plt.xlabel('Index')
plt.ylabel('Square')
# This code is required for the autofeedback, don't delete it!
fighand = plt.gca()

plt.figure()
xvals = np.zeros(20)
yvals = np.zeros(20)
for i in range(20) : 
    xvals[i] = i
    yvals[i] = (1/2)**i
plt.plot( xvals, yvals, 'ko' )
plt.xlabel('Index')
plt.ylabel('Geometric series')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

plt.figure()
xvals = np.linspace(0,99,100)
triangularNumbers = np.zeros(100)
# Insert your code to compute the triangular numbers here
for i in range(1, 100):
    triangularNumbers[i] = triangularNumbers[i-1] + i
plt.plot( xvals, triangularNumbers, 'ko' )
plt.xlabel('Index')
plt.ylabel('Triangular Numbers')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()

plt.figure()
xvals = np.zeros(100)
fibonacci = np.zeros(100)
# Insert your code for the fibonacci series here
xvals[0], xvals[1] = 1, 2
fibonacci[0] = fibonacci[1] = 1
for i in range(2,100) : 
    xvals[i] = i+1
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
plt.plot( xvals, fibonacci, 'ko' )
plt.xlabel("Index")
plt.ylabel("Fibonacci series")
fighand = plt.gca()

x = -3
y = 2
z = -6
if x<0 : fx = -1*x
else : fx = x
if y<0 : fy = -1*y
else : fy = y    
if z<0 : fz = -1*z
else : fz = z

# This loads the data from values.dat into the NumPy array called xvals
xvals = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Programming/values.dat')
yvals = np.zeros(len(xvals))
for i in range(len(xvals)):
    if xvals[i]<0 : yvals[i] = -1*xvals[i]
    else : yvals[i] = xvals[i]

# This loads the data into a NumPy array called xvals
xvals = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Programming/mydata.dat')
yvals = np.zeros(len(xvals))
for i in range(len(xvals)) : 
    if xvals[i]==5 : yvals[i]=1
    else : yvals[i] = 0
print(xvals)


# This loads the data into a NumPy array called xvals
xvals = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Programming/mydata.dat')
# Add code so that this variable is set equal to the number of fives in xvals
nfives=0
for d in xvals : 
    if d==5 : nfives += 1

# This loads the data into a NumPy array called xvals
xvals = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Programming/mydata.dat')
# Add code so that these variables are set equal to the number of elements in
# xvals that are less than or equal to five and that are more than five respectively
nlefive=0
nmefive=0
for d in xvals : 
    if d<=5 : nlefive += 1
    if d>= 5 : nmefive += 1

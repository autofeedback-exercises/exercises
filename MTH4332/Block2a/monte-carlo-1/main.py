def incircle(x,y) :
  # Your code goes here
  
  return 

npoints = 100
gridspacing = 1.0/npoints
npoints_in_circle = 0
for i in range(npoints) :
  x = (i+0.5)*gridspacing
  for j in range(npoints) :
    y = (j+0.5)*gridspacing
    npoints_in_circle = npoints_in_circle + incircle(x,y)
    
final_integral = npoints_in_circle / (npoints*npoints)
print( final_integral )

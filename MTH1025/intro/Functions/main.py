# write your code here
import numpy as np
def hemi_volume(radius):
    return (2./3.)*np.pi*radius**3.
def cone_volume(radius,height):
    return np.pi*radius*radius*height/3.0
def compound_volume(radius,height):
    return cone_volume(radius,height) + hemi_volume(radius)

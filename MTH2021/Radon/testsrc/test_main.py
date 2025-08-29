import numpy as np
import AutoFeedback.varchecks as vc
from AutoFeedback.utils import get_internal as get
import unittest

def sheplog(N):
    #
    # Toft's modified Shepp-Logan picture
    #
    #
    # It is created as a list of ellipses
    # Each entry in Elli describes a separate ellipse
    # Parameters: center x, center y
    #             minor r, major r
    #             angle w.r.t. y, shading value
    #
    # original shading values: 
    # 2 -.98 -0.02 -0.02 remainder 0.01
    #
    # modified:
    # 1 -.8 -.2 -.2 others .1
    #
    Elli=[]
    Elli.append((0,0,0.69,0.92,0,1))
    Elli.append((0,-0.0184,0.6624,0.874,0,-0.8))
    Elli.append((0.22,0,0.11,0.31,-18,-0.2))
    Elli.append((-0.22,0,0.16,0.41,18,-0.2))
    Elli.append((0,0.35,0.21,0.25,0,0.1))
    Elli.append((0,0.1,0.046,0.046,0,0.1))
    Elli.append((0,-0.1,0.046,0.046,0,0.1))
    Elli.append((-0.08,-0.605,0.046,0.023,0,0.1))
    Elli.append((0,-0.605,0.023,0.023,0,0.1))
    Elli.append((0.06,-0.605,0.023,0.046,0,0.1))
    slimg=np.zeros((N,N))
    xcoord = np.linspace(1,-1,N)
    ycoord = np.linspace(-1,1,N)
    for component in Elli:
        xcent=component[0]
        ycent=component[1]
        xlen=component[3]
        ylen=component[2]
        angle= component[4]
        gray = component[5]
        for j in range(N):
            for k in range(N):
                x=(xcoord[j]-ycent)*np.cos(angle/180*np.pi)-(ycoord[k]-xcent)*np.sin(angle/180*np.pi)
                y=(ycoord[k]-xcent)*np.cos(angle/180*np.pi)+(xcoord[j]-ycent)*np.sin(angle/180*np.pi)
                if ((((x)/xlen)**2+((y)/ylen)**2)<=1.):
                    slimg[j,k] += gray
    return slimg



class UnitTests(unittest.TestCase) :
    def test_kgrid(self):
        N = get('N')
        assert vc.check_vars('k_grid', [ii*np.pi for ii in range(N//2+1)] + [ -ii*np.pi for ii in range(N//2-1, 0, -1)])

    def test_absk(self):
        k_grid = get('k_grid')
        assert vc.check_vars('abs_k', np.abs(k_grid))

    def test_phasek(self):
        k_grid = get('k_grid')
        assert vc.check_vars('phase_k', np.exp(-1j*k_grid))
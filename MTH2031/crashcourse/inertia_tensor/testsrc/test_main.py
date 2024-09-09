from AutoFeedback import check_vars
import unittest
import numpy as np
from AutoFeedback.randomclass import randomvar
from AutoFeedback.utils import get_internal as get


class UnitTests(unittest.TestCase):
    def test_vars(self):
        assert check_vars('m', np.ones(100))
        myvar = randomvar(
            nsamples=100,
            expectation=0.0,
            dist="normal",
            variance=1.0,
            isinteger=False,
        )
        assert check_vars("x", myvar)
        myvar = randomvar(
            nsamples=100,
            expectation=0.0,
            dist="normal",
            variance=4.0,
            isinteger=False,
        )
        assert check_vars("y", myvar)
        myvar = randomvar(
            nsamples=100,
            expectation=0.0,
            dist="normal",
            variance=9.0,
            isinteger=False,
        )
        assert check_vars("z", myvar)

    def test_vars_2(self):
        assert check_vars("M", 100)
        x, y, z = get("x"), get("y"), get("z")
        Xc = 0.01 * np.sum(x)
        Yc = 0.01 * np.sum(y)
        Zc = 0.01 * np.sum(z)
        x1 = x - Xc
        y1 = y - Yc
        z1 = z - Zc
        assert check_vars("Xc", Xc)
        assert check_vars("Yc", Yc)
        assert check_vars("Zc", Zc)
        assert check_vars("x1", x1)
        assert check_vars("y1", y1)
        assert check_vars("z1", z1)

    def test_tensor(self):
        I = np.zeros((3,3))
        m, x1, y1, z1 = get('m'), get('x1'), get('y1'), get('z1')
        I[0,0] = np.sum( m * (y1**2 + z1**2))
        I[1,1] = np.sum( m * (x1**2 + z1**2))
        I[2,2] = np.sum( m * (x1**2 + y1**2))
        I[0,1] = -np.sum( m * x1 * y1)
        I[0,2] = -np.sum( m * x1 * z1)
        I[1,2] = -np.sum( m * y1 * z1)
        I[1,0] = I[0,1]
        I[2,0] = I[0,2]
        I[2,1] = I[1,2]
        assert check_vars('I', I)


def plot_system(m, x, y, z):
    import numpy as np
    import matplotlib.pyplot as plt

    N = len(m)
    assert len(x) == N, "x is not the correct length"
    assert len(y) == N, "y is not the correct length"
    assert len(z) == N, "z is not the correct length"
    M = np.sum(m)
    Xc = np.sum(m*x)/M
    Yc = np.sum(m*y)/M
    Zc = np.sum(m*z)/M
    x1 = x - Xc
    y1 = y - Yc
    z1 = z - Zc
    I = np.zeros((3,3))
    I[0,0] = np.sum( m * (y1**2 + z1**2))
    I[1,1] = np.sum( m * (x1**2 + z1**2))
    I[2,2] = np.sum( m * (x1**2 + y1**2))
    I[0,1] = -np.sum( m * x1 * y1)
    I[0,2] = -np.sum( m * x1 * z1)
    I[1,2] = -np.sum( m * y1 * z1)
    I[1,0] = I[0,1]
    I[2,0] = I[0,2]
    I[2,1] = I[1,2]
    
    Ipr, Vpr = np.linalg.eig(I)

    ax = plt.axes(projection='3d')
    for xx, yy, zz, mm in zip(x, y, z, m):
        ax.plot3D(xx, yy, zz,'m.', markersize=10*mm)
        ax.plot3D(Xc, Yc, Zc,'r.')

    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # Scaling factors have the dimension length, proportional
    # to sqrt of the principal moments of inertia

    S1 = np.sqrt(Ipr[0]/M)
    S2 = np.sqrt(Ipr[1]/M)
    S3 = np.sqrt(Ipr[2]/M)

    # Checking eigenvector normalisation and orthogonality
    # print(np.sum(Vpr[:,0]**2),np.sum(Vpr[:,0]*Vpr[:,1]))

    ax.quiver(Xc,Yc,Zc,S1*Vpr[0,0],S1*Vpr[1,0],S1*Vpr[2,0], color='r', arrow_length_ratio = 0.3)
    ax.quiver(Xc,Yc,Zc,S2*Vpr[0,1],S2*Vpr[1,1],S2*Vpr[2,1], color='g', arrow_length_ratio = 0.3)
    ax.quiver(Xc,Yc,Zc,S3*Vpr[0,2],S3*Vpr[1,2],S3*Vpr[2,2], color='b', arrow_length_ratio = 0.3)

    plt.show()
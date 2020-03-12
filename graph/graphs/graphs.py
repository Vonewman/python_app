 
"""This generates four graphs for arcsin(z)."""
# Original: Peter Halasz. 2010-09-14
# Enhanced: Ika. 2013-07-23
 
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
 
graphs = {'abs':abs, 'real':real, 'imag':imag, 'angle':angle}
 
for gr in graphs:
    ax = Axes3D(figure(), azim = -135, elev = 45)
    X = arange(-2*pi, 2*pi, pi/12)
    Y = arange(-4, 4, .2)
    X, Y = meshgrid(X, Y)
    fn = graphs[gr]
    Z = fn(arcsin(X + Y*1j))  # abs, real, imag, angle. angle range [-pi, pi]
    ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.jet)
    ax.contour(X, Y, Z, zdir='z', offset=np.min(Z))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel(gr + '(sin(x+iy))')
    plt.savefig("complex_arcsin_" + gr + "_01_Pengo.jpg")

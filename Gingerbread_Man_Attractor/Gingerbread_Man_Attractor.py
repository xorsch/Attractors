""" https://www.softology.com.au/tutorials/attractors2d/tutorial.htm

    The Gingerbread Man attractor (named for the obvious gingerbread man like shape it creates) 
    is a simple example that does not have any parameters to change.

    The formula to create this attractor is

    newx = 1 - y + abs(x)
    newy = x

    The initial x value is set to -0.1 and the initial y value is set to 0.
"""
import sys
import numpy
import matplotlib.pyplot as plt
from numba import jit
from PIL import Image


@jit( nopython=True )
def Gingerbread_create( iterations ):

    Gingerbread = numpy.zeros( ( 2, iterations ) )
    Gingerbread[0][0]=  0.10
    Gingerbread[1][0]=  0.01
    
    return Gingerbread


@jit( nopython=True )
def Gingerbread_calc( Gingerbread, iterations ):

    a  = 2.300
    b  = 2.200
    c  = 1.950 # 1.010 # 2.000
    dt = 1.000 # 0.950
    
    for n in range ( 1, iterations ):

        Gingerbread[0][n] = c - numpy.cos( a * Gingerbread[1][n-1] * dt ) + numpy.abs( numpy.sin( b * Gingerbread[0][n-1] * dt ) )
        Gingerbread[1][n] = Gingerbread[0][n-1] * dt

    return Gingerbread


def main():

    iterations = 10000000

    Gingerbread = Gingerbread_create( iterations )
    Gingerbread = Gingerbread_calc( Gingerbread, iterations )

    plt.plot( Gingerbread[0], Gingerbread[1], "g,", alpha=0.1 )
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    
    main()

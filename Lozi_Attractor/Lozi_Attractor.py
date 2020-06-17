
""" https://www.softology.com.au/tutorials/attractors2d/tutorial.htm

    The formula to create this attractor is

    newx = 1 - y + abs( a * x + b * y)
    newy = x

    The initial x value is set to -0.1 and the initial y value is set to 0.
"""
import sys
import numpy
import matplotlib.pyplot as plt
from numba import jit
from PIL import Image


@jit( nopython=True )
def Lozi_create( iterations ):

    lozi = numpy.zeros( ( 2, iterations ) )
    lozi[0][0]=  0.4
    lozi[1][0]=  0.025
    
    return lozi

@jit( nopython=True )
def Lozi_calc( lozi, iterations ):

    a  = -1.500
    b  =  0.800

    
    for n in range ( 1, iterations ):

        lozi[0][n] = 1 - numpy.abs( a * lozi[0][n-1] +  b * lozi[1][n-1] )
        lozi[1][n] = lozi[0][n-1]

    return lozi


def main():

    iterations = 100000000

    lozi = Lozi_create( iterations )
    lozi = Lozi_calc( lozi, iterations )

    plt.plot( lozi[0], lozi[1], ",", alpha=0.1 )
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    
    main()

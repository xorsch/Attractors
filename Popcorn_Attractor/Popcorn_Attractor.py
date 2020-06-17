""" https://www.softology.com.au/tutorials/attractors2d/tutorial.htm

	The Popcorn attractor also comes Cliff Pickover.

	The formula to create these attractors is

	newx = x - h * sin( y + tan( tangentfactor * y ) )
	newy = y - h * sin( x + tan( tangentfactor * x ) )

	Each point on the display area is used for the starting X and Y values. 
	The xnew and ynew values are repeated for a number of iterations. 
	The tangent factor value changes the detail of the images created.

	Here are a few more sample images of what this formula can produce.

	NOTA: no s'ha pogut reproduir el patró de les imatges!!!

"""

import numpy
import matplotlib.pyplot as plt
from numba import jit


@jit( nopython=True )
def Popcorn_create( iterations ):

	Popcorn = numpy.zeros( ( 2, iterations ) )
	Popcorn[0][0]= -0.400 #0.6
	Popcorn[1][0]=  0.001 #0.2

	return Popcorn


@jit( nopython=True )
def Popcorn_calc( Popcorn, iterations ):

        a = -0.510
        b =  2.350
        l =  0.000
        
        for n in range ( 1, iterations ):
                
                Popcorn[0][n] = l * Popcorn[0][n-1] - a * numpy.sin( Popcorn[1][n-1] + numpy.tan( b * Popcorn[1][n-1] ) )
                Popcorn[1][n] = l * Popcorn[1][n-1] - a * numpy.sin( Popcorn[0][n-1] + numpy.tan( b * Popcorn[0][n-1] ) )
		
        return Popcorn


iterations = 500000

def main():

	Popcorn = Popcorn_create( iterations )
	Popcorn = Popcorn_calc( Popcorn, iterations )

	plt.plot( Popcorn[0], Popcorn[1], ",", lw=0.1, alpha=.5 )
	plt.axis('equal')
	plt.show()

if __name__ == "__main__":
	main()


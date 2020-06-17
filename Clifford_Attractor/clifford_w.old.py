''' https://en.wikipedia.org/wiki/Clifford_A._Pickover
    https://softologyblog.wordpress.com/2017/03/04/2d-strange-attractors/


    http://paulbourke.net/fractals/clifford/
 
    a = -1.400, b =  1.600  c =  1.000, d =  0.700
    a =  1.600, b = -0.600, c = -1.200, d =  1.600
    a =  1.700, b =  1.700, c =  0.600, d =  1.200
    a =  1.500, b = -1.800, c =  1.600, d =  0.900
    a = -1.700, b =  1.300, c = -0.100, d = -1.200
    a = -1.700, b =  1.800  c = -1.900, d = -0.400
    a = -1.800, b = -2.000  c = -0.500, d = -0.900
    a = -1.700, b =  1.300, c = -0.100, d = -1.210
    a = -1.700, b =  1.800, c = -0.900, d = -0.400
    a =  1.500, b = -1.800, c =  1.600, d =  2.000
    a = -2.239, b = -2.956, c =  1.272, d =  1.419
    a = -1.700, b =  1.800, c = -1.900, d = -0.400
    
    
    http://paulbourke.net/fractals/peterdejong/ c*(-1) i d*(-1)

    a =  1.641, b =  1.902, c =  0.316, d=   1.525
    a =  0.970, b = -1.899, c =  1.381, d = -1.506
    a =  1.400, b = -2.300, c =  2.400, d = -2.100
    a =  2.010, b = -2.530, c =  1.610, d = -0.330
    a = -2.700, b = -0.090, c = -0.860, d = -2.200
    a = -0.827, b = -1.637, c =  1.659, d = -0.943
    a = -2.240, b =  0.430, c = -0.650, d = -2.430
    a = -2,000, b = -2.000, c = -1.200, d =  2.000
    a = -0.709, b =  1.638, c =  0.452, d =  1.740
'''
import sys
import numpy
import matplotlib.pyplot as plt
from numba import jit
from PIL import Image

class Point:

    def __init__(self):
        self.x = 0.0;
        self.y = 0.0;

    def setPointX(self, x ):
        self.x = x

    def setPointY(self, y ):
        self.y = y

    def setPoint(self, x, y ):
        self.x = x
        self.y = y

    def getPointX(self):
        return self.x

    def getPointY(self):
        return self.y

    def getPoint(self):
        return self.x, self.y


@jit(nopython=True)
def calculate_X( a, cy, c, cx):
    return numpy.sin( a * cy ) + c * numpy.cos( a * cx )


@jit(nopython=True)
def calculate_Y( b, cx, d, cy):
    return numpy.sin( b * cx ) + d * numpy.cos( b * cy )


@jit(nopython=True)
def position_X( w2, w, cx, ax):

    return ( w2 + ( ( w  * cx)  / ( ax ) ) )


@jit(nopython=True)
def position_Y( h2, h, cy, ay):
    return ( h2 + ( ( h  * cy ) / ( ay )  ) )


def main():

    x_min, x_max = -2.00, 2.25
    y_min, y_max = -2.00, 2.00
    Ax_view = x_max - x_min
    Ay_view = y_max - y_min 

    width  = 1920
    height = 1920

    width_2  = width/2
    height_2 = height/2

    iterations = 100000000

    a = -1.400
    b =  1.600
    c =  1.000
    d =  0.700

    cliffordNew = Point()
    cliffordOld = Point()
    cliffordOld.setPoint( .01, .01 )
    temp_image = numpy.zeros( [width,height], dtype='float64' )
    image      = Image.new( 'RGB', (width,height), color=0 )
    L_max = 0
    n = 1

    while( (n<iterations) ): # and (L_max<255)
        
        sys.stdout.write(f'\rCreant attractor {round((n*100/iterations),2)}%  ') # {round((L_max*100/255),2)}%
        
        cliffordNew.setPointX( calculate_X( a, cliffordOld.getPointY(), c, cliffordOld.getPointX() ) )
        cliffordNew.setPointY( calculate_Y( b, cliffordOld.getPointX(), d, cliffordOld.getPointY() ) )
        
        pos_x = int( position_X( width_2,  width,  cliffordNew.getPointX(), Ax_view ) )
        pos_y = int( position_Y( height_2, height, cliffordNew.getPointY(), Ay_view ) )

        temp_image[ ( pos_x, pos_y) ] = temp_image[ ( pos_x, pos_y ) ] + 1

        if( L_max < temp_image[ (pos_x, pos_y ) ] ):
            L_max = temp_image[ (pos_x, pos_y ) ]
    
        C = int( temp_image[ ( pos_x, pos_y ) ] )
        image.putpixel( ( pos_x, pos_y ), ( C, C, C ) )

        cliffordOld.setPoint( cliffordNew.getPointX(), cliffordNew.getPointY() )
        n = n + 1

    image.save('symetric_gray.png')
    print("max ", L_max )

if __name__ == "__main__":
    
    main()

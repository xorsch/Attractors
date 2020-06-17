''' https://en.wikipedia.org/wiki/Clifford_A._Pickover

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
def calculate_X( pop_x, pop_y, a, b, l ):
    return l * pop_x + a * numpy.sin( pop_y + numpy.tan( b * pop_y ) )


@jit(nopython=True)
def calculate_Y( pop_x, pop_y, a, b, l ):
    return l * pop_y + a * numpy.sin( pop_x + numpy.tan( b * pop_x ) )


@jit(nopython=True)
def position_X( w2, w, cx, ax):

    return ( w2 + ( ( w  * cx)  / ( ax ) ) )


@jit(nopython=True)
def position_Y( h2, h, cy, ay):
    return ( h2 + ( ( h  * cy ) / ( ay )  ) )


def main():

    x_min, x_max = -0.75, 0.75
    y_min, y_max = -0.75, 0.75
    
    Ax_view = x_max - x_min
    Ay_view = y_max - y_min 

    width  = 3500
    height = 3500

    width_2  = width /2
    height_2 = height/2

    iterations = 16581375
    # 1000000000
    

    a = -0.510
    b =  2.350
    l =  0.000
     

    popCornNew  = Point()
    popCorndOld = Point()
    popCorndOld.setPoint( -0.400, 0.001 )
    temp_image = numpy.zeros( [width,height], dtype='float64' )
    image      = Image.new( 'RGB', (width,height), color=0 )
    n = 1

    while( n < iterations ):
        
        sys.stdout.write(f'\rCreant attractor {round((n*100/iterations),2)}%  ')
        
        popCornNew.setPointX( calculate_X( popCorndOld.getPointY(), popCorndOld.getPointX(), a, b, l  ) )
        popCornNew.setPointY( calculate_Y( popCorndOld.getPointY(), popCorndOld.getPointX(), a, b, l  ) )
        
        pos_x = int( position_X( width_2,  width,  popCornNew.getPointX(), Ax_view ) )
        pos_y = int( position_Y( height_2, height, popCornNew.getPointY(), Ay_view ) )

        if( pos_x > -1 and pos_x < width and pos_y > -1 and pos_y < height):
            temp_image[ ( pos_x, pos_y) ] = temp_image[ ( pos_x, pos_y ) ] + 64
            C = int( temp_image[ ( pos_x, pos_y ) ] )
            n = n + 1

        popCorndOld.setPoint( popCornNew.getPointX(), popCornNew.getPointY() )


    for ny in range( height):

        sys.stdout.write(f'\rTransform gray scale {round((ny*100/height),2)}%  ')
        sys.stdout.flush()
			
        for nx in range ( width ):

            color = int( temp_image[(nx,ny)] )
				
            if( color<255 ):
                colorRGB = (color,0,0)
            elif( color<65025 ):
                colorRGB = ( 255, int((color-255)/255), 0 )
            elif( color<16581375 ):
                colorRGB = ( 255, 255, int((color-65025)/(65025)) )

            image.putpixel( (nx,ny) , colorRGB )
                

    image.save('symetric_gray.png')

if __name__ == "__main__":
    
    main()

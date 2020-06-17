
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
from numba import jit
from PIL import Image

x_min, x_max = -2.00, 2.50
y_min, y_max = -2.00, 2.00

@jit( nopython=True )
def clifford_create( iterations ):

    clifford = numpy.zeros( ( 2, iterations ) )
    clifford[0][0]=.01
    clifford[1][0]=.01

    return clifford


@jit( nopython=True )
def clifford_calc( clifford, iterations, a, b, c, d ):
    
    for n in range ( 1, iterations ):
        
        clifford[0][n] = numpy.sin( a * clifford[1][n-1] ) + c * numpy.cos( a * clifford[0][n-1] )
        clifford[1][n] = numpy.sin( b * clifford[0][n-1] ) + d * numpy.cos( b * clifford[1][n-1] )

    return clifford


@jit( nopython=True )
def fpos_x( clifford, width, Ax_width ):

    return int(  width/2 + ( width*clifford  / Ax_width  ) )


@jit( nopython=True )
def fpos_y( clifford, height, Ay_height ):

    return int( height/2 + ( height*clifford / Ay_height ) )


iterations = 1000000000

a = -1.800 # a = -1.400
b = -2.000 # b =  1.600
c = -0.500 # c =  1.000
d = -0.900 # d =  0.700


def main():

    clifford = clifford_create( iterations )
    clifford = clifford_calc( clifford, iterations, a, b, c, d )

    width  = 1920
    height = 1920

    """ Calcula els colors de l'atractor i guarda el valor màxim
    """

    temp_image = numpy.zeros( [width,height] )

    Ax_width  = x_max - x_min
    Ay_height = y_max - y_min
    L_max = 0

    for n in range ( iterations ):

        sys.stdout.write(f'\rRendering {round((n*100/iterations),2)}% ')

        pos_x = fpos_x( clifford[0][n], width,  Ax_width  )
        pos_y = fpos_y( clifford[1][n], height, Ay_height ) 

        temp_image[ ( pos_x, pos_y ) ] = temp_image[ ( pos_x, pos_y ) ] + 32

        if( temp_image[ ( pos_x, pos_y ) ] > L_max ):
            L_max = temp_image[ ( pos_x, pos_y ) ]



    """ Aumenta el contrast de l'imatge
    """

    image = Image.new( 'RGB', (width,height), color=0 )
    scale = 255.0/L_max
    L_max = 0.0

    for pos_x in range (width):

        sys.stdout.write(f'\rEqualitzant {round((pos_x*100/width),2)}% ')

        for pos_y in range (height):

            C = int( temp_image[ (pos_x, pos_y ) ] * scale )
            if ( L_max < C ):
                L_max = C

            image.putpixel( (pos_x, pos_y ), (C, C, C) )
    
    print( "max ", L_max )
    image.save('symetric_gray.png')

if __name__ == "__main__":

    main()

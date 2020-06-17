'''
    https://softologyblog.wordpress.com/2017/03/04/2d-strange-attractors/
    http://sprott.physics.wisc.edu/pubs/paper219.htm
    http://www.fractalsciencekit.com/tutorial/examples/symicon.htm
    Symmetric Icon Attractor

    These attractors came from the book “Symmetry in Chaos” by Michael Field and Martin Golubitsky. 
    They give symmetric results to the attractors formed.

    L = -2.500  A =  5.000  B =  -1.900  G =  1.000  O =  0.188  D =  5.000
    L =  1.560  A = -1.000  B =   0.100  G = -0.820  O =  0.120  D =  3.000
    L = -1.806  A =  1.806  B =   0.000  G =  1.000  O =  0.000  D =  5.000
    L = -2.195  A = 10.000  B = -12.000  G =  1.000  O =  0.000  D =  3.000
    L = -2.050  A =  3.000  B = -16.790  G =  1.000  O =  0.000  D =  9.000
    L = -2.700  A =  5.000  B =   1.500  G =  1.000  O =  0.000  D =  6.000
    L =  2.409  A = -2.500  B =   0.000  G =  0.900  O =  0.000  D = 23.000
    L = -2.080  A =  1.000  B =  -0.100  G =  0.167  O =  0.000  D =  7.000
    L = -2.320  A =  2.320  B =   0.000  G =  0.750  O =  0.000  D =  5.000
    L =  2.600  A = -2.000  B =   0.000  G = -0.500  O =  0.000  D =  5.000
    L = -2.340  A =  2.000  B =   0.200  G =  0.100  O =  0.000  D =  5.000
    L = -1.860  A =  2.000  B =   0.000  G =  1.000  O =  0.100  D =  4.000
    L =  1.560  A = -1.000  B =   0.100  G = -0.820  O =  0.000  D =  3.000
    L =  1.500  A = -1.000  B =   0.100  G = -0.805  O =  0.000  D =  3.000
    L =  1.455  A = -1.000  B =   0.030  G = -0.800  O =  0.000  D =  3.000
    L =  2.390  A = -2.500  B =  -0.100  G =  0.900  O = -0.150  D = 16.000

'''
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# ventana del atractor
x_min, x_max = -1.21, 1.21
y_min, y_max = -1.21, 1.21

# x and y both start at 0.01
x,y = 0.01, 0.01

lanbda =  2.390
alpha  = -2.500
beta   = -0.100 
gamma  =  0.900
omega  = -0.150
degree = 19.000

n = 2
iterations = 20000000
sa = np.zeros( (2,iterations) )
sa[0][0], sa[1][0] = x, y


sys.stdout.write(f'Creating image\n')

while( n < iterations ):

    sys.stdout.write(f'\rIteration {round((n*100/iterations),1)}%  ')
    sys.stdout.flush()

    p = alpha *( x**2 + y**2 ) + lanbda
    zreal, zimag = x, y

    for i in range( int(degree - 2) ):
        za, zb = zreal * x - zimag * y, zimag * x + zreal * y
        zreal, zimag = za, zb

    p  = p + beta * ( x * zreal - y * zimag )

    xnew, ynew = ( p * x + gamma * zreal - omega * y ), ( p * y - gamma * zimag + omega * x )
    x, y  = xnew, ynew

    if( ( x > x_min and x < x_max ) and ( y > y_min and y < y_max ) ):
        sa[0][n-1], sa[1][n-1] = x, y
        n = n + 1

# Creant imatge
width  = 3800
height = 3800
image  = Image.new( 'RGB', (width,height), color=0 )

sys.stdout.write(f'\nRendering image\n')

for n in range ( iterations ):

    sys.stdout.write(f'\rIteration {round((n*100/iterations),1)}%  ')
    sys.stdout.flush()

    x, y  = sa[0][n], sa[1][n]
    pos_x = int( width/2  + (( width  * x ) / ( x_max - x_min )) )
    pos_y = int( height/2 + (( height * y ) / ( y_max - y_min )) )

    L = image.getpixel( ( pos_x , pos_y) )
    image.putpixel( ( pos_x, pos_y ), (L[0]+8, L[1]+8, L[2]+8) )

#image.show()
image.save('symetric.png')

sys.stdout.write(f'Saved image\n')

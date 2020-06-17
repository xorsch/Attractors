# https://en.wikipedia.org/wiki/Clifford_A._Pickover
# https://softologyblog.wordpress.com/2017/03/04/2d-strange-attractors/
# http://paulbourke.net/fractals/wallpaper/

# The Hopalong attractor was discovered by Barry Martin.
# x and y both start at 0
#
# xnew = y - 1 - sqrt( abs(b*x-1-c) ) * sign(x-1)
# ynew = a - x - 1
#
# The parameters a, b and c can be any floating point value between 0 and +10.
#
# a=7.16878197155893 b=8.43659746693447  c=2.55983412731439
# a=7.7867514709942  b=0.132189802825451 c=8.14610984409228
# a=9.74546888144687 b=1.56320227775723  c=7.86818214459345
# a=9.8724800767377  b=8.66862616268918  c=8.66950439289212
# a=9.7671244922094  b=4.10973468795419  c=3.78332691499963

import numpy as np
from numba import jit
import matplotlib.pyplot as plt


@jit(nopython=True)
def Hopalong_create( size ):

    Hopalong = np.zeros( ( 2,size ) )

    return Hopalong



@jit(nopython=True)
def Hopalong_calc( Hopalong, iterations ):

    a = 7.78675147099421  
    b = 0.13218980282545 
    c = 8.14610984409228
    D = 1.0
    E = 1.0

##    x_max = -1000.0
##    x_min =  1000.0
##    y_max = -1000.0
##    y_min =  1000.0

    for n in range ( 2,iterations ): 

        Hopalong[0][n] =     Hopalong[1][n-1] - E - np.sqrt( np.abs((b * Hopalong[0][n-1] - D - c)) ) * np.sign((Hopalong[0][n-1]-D))
        Hopalong[1][n] = a - Hopalong[0][n-1] - E

##        if( x_min > Hopalong[0][n] ):
##            x_min = Hopalong[0][n]
##            
##        if( x_max < Hopalong[0][n] ):
##            x_max = Hopalong[0][n]
##            
##        if( y_min > Hopalong[1][n] ):
##            y_min = Hopalong[1][n]
##            
##        if( y_max < Hopalong[1][n] ):
##            y_max = Hopalong[1][n]
##
##    print("X [",x_min, ", ", x_max, "] - Y [", y_min, ",", y_max, "]" )
            
    return Hopalong



hopalong = Hopalong_create( size=1000000 )
hopalong = Hopalong_calc( hopalong, hopalong.shape[1] )



plt.plot( hopalong[0], hopalong[1], ",", alpha=0.1 )
plt.axis( 'equal' )
plt.savefig( 'Hopalong.png', format='png', dpi=500 )
plt.show()


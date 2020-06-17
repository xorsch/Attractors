
import numpy as np
import matplotlib.pyplot as plt
from numba import jit


@jit(nopython=True)
def LorenzInit( num_steps, x, y, z ):

    lorenz = np.zeros( (3,num_steps+1) )
 
    lorenz[0][0] = x
    lorenz[1][0] = y
    lorenz[2][0] = z

    return lorenz


@jit(nopython=True)
def LorenzCalc( lorenz, dt, s, r, b ):

    for i in range (lorenz.shape[1]-1):
    
        lorenz[0][i+1] = lorenz[0][i] + ( ( s * (lorenz[1][i] - lorenz[0][i]) ) * dt )
        lorenz[1][i+1] = lorenz[1][i] + ( ( lorenz[0][i] * ( r - lorenz[2][i] ) - lorenz[1][i]) * dt )
        lorenz[2][i+1] = lorenz[2][i] + ( ( lorenz[0][i] * lorenz[1][i] - b * lorenz[2][i] ) * dt )

    return lorenz


def main():
    num_steps=10000000

    ts = np.arange( 0, num_steps+1, 1 )

    lorenz = LorenzInit( num_steps, x=0.0,  y=1.0,  z=1.05 )
    lorenz = LorenzCalc( lorenz, dt=0.0001, s=10.0, r=28.0, b=(8.0/3.0) )

    fig, [ax1, ax2, ax3] = plt.subplots( 3, 1, sharex=True )
    fig.suptitle( "Lorenz Attractors " )
    ax1.plot( ts, lorenz[0], 'r,', lw=2 )
    ax2.plot( lorenz[1], 'g,', lw=2 )
    ax3.plot( lorenz[2], 'b,', lw=2 )

    ax1.set_title( 'x axis', loc='left' )
    ax2.set_title( 'y axis', loc='left' )
    ax3.set_title( 'z axis', loc='left' )

    ax1.grid( True )
    ax2.grid( True )
    ax3.grid( True )

    plt.show()

if __name__ == "__main__":
    main()



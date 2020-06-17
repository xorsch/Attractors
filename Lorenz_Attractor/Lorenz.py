
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

    lorenz = LorenzInit( num_steps=100000000, x=0.0,  y=1.0,  z=1.05 )
    lorenz = LorenzCalc( lorenz, dt=0.0001, s=10.0, r=28.0, b=(8.0/3.0) )

    fig = plt.figure()
    ax  = fig.gca( projection='3d' )
    ax.plot( lorenz[0], lorenz[1], lorenz[2], lw=0.5 )
    plt.show()

if __name__ == "__main__":
    main()


import numpy as np
from numba import jit
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)


@jit(nopython=True)
def strangeAttractor( x, y, z, a = 3.0, b = 2.2, v = 1.0, u = 0.001):

    x_dot =  a * x * (1 - y) - b * z
    y_dot = -v * y * (1 - x * x)
    z_dot =  u * x

    return x_dot, y_dot, z_dot


dt = 0.002
num_steps = 500000

ts = np.arange( 0, num_steps + 1 )
xs = np.empty( num_steps + 1 )
ys = np.empty( num_steps + 1 )
zs = np.empty( num_steps + 1 )

xs[0], ys[0], zs[0] = ( 1.0, 1.0, 0.0 )

for i in range ( num_steps ):

    x_dot, y_dot, z_dot = strangeAttractor( xs[i], ys[i], zs[i] )

    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)


fig, [ax1, ax2, ax3] = plt.subplots( 3, 1, sharex=True )
fig.suptitle( "Strange Attractors " )
ax1.plot( ts, xs, 'r,', lw=2 )
ax2.plot( ys, 'g,', lw=2 )
ax3.plot( zs, 'b,', lw=2 )

ax1.set_title( 'x axis', loc='left' )
ax2.set_title( 'y axis', loc='left' )
ax3.set_title( 'z axis', loc='left' )

ax1.grid( True )
ax2.grid( True )
ax3.grid( True )

# Setting x axis
ax1.xaxis.set_major_locator( MultipleLocator(50000) )
ax1.xaxis.set_major_formatter( FormatStrFormatter('%d') )
ax1.xaxis.set_minor_locator( MultipleLocator(10000) )

# Setting y axis
ax1.yaxis.set_major_locator( MultipleLocator(1 ) )
ax1.xaxis.set_major_formatter( FormatStrFormatter('%d') )
ax1.yaxis.set_minor_locator( MultipleLocator(.5) )

ax2.yaxis.set_major_locator( MultipleLocator(1 ) )
ax2.xaxis.set_major_formatter( FormatStrFormatter('%d') )
ax2.yaxis.set_minor_locator( MultipleLocator(.5) )

ax3.yaxis.set_major_locator( MultipleLocator(.05 ) )
ax3.xaxis.set_major_formatter( FormatStrFormatter('%d') )
ax3.yaxis.set_minor_locator( MultipleLocator(.025) )

plt.show()

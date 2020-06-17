'''http://chaos-3d.e-monsite.com/pages/strange-attractor-type-iv.html
'''

import numpy as np
import matplotlib.pyplot as plt
from numba import jit

@jit(nopython=True)
def strangeAttractor( x, y, z, a = 2.0, b = -3.0, o = 0.8, u = 1.0, n = -2.0, s = 0.3 ):

    x_dot = a * x * ( y - 1 ) + ( b * y * z )
    y_dot = o * ( 1 - x * x ) * y + ( u * x * z )
    z_dot = ( n * x * y ) + ( s * z )

    return x_dot, y_dot, z_dot


dt = 0.001
num_steps = 50000

xs = np.empty( num_steps + 1 )
ys = np.empty( num_steps + 1 )
zs = np.empty( num_steps + 1 )

xs[0], ys[0], zs[0] = ( 0.5, -1.0, 0.5 )

for i in range ( num_steps ):

    x_dot, y_dot, z_dot = strangeAttractor( xs[i], ys[i], zs[i] )

    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)


# Plot
fig = plt.figure()
ax = fig.gca( projection='3d' )

ax.plot( xs, ys, zs, lw=0.35 )
ax.set_xlabel( "X Axis")
ax.set_ylabel( "Y Axis" )
ax.set_zlabel( "Z Axis" )
ax.set_title("Strange Attractor Type I")

plt.show()

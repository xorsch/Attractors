'''http://chaos-3d.e-monsite.com/pages/page.html
'''

import numpy as np
import matplotlib.pyplot as plt
from numba import jit

@jit(nopython=True)
def strangeAttractor( x, y, z, a = 3.0, b = 2.2, v = 1.0, u = 0.001):

    x_dot =  a * x * (1 - y) - b * z
    y_dot = -v * y * (1 - x * x)
    z_dot =  u * x

    return x_dot, y_dot, z_dot


dt = 0.002
num_steps = 2000000

xs = np.empty( num_steps + 1 )
ys = np.empty( num_steps + 1 )
zs = np.empty( num_steps + 1 )

xs[0], ys[0], zs[0] = ( 1.0, 1.0, 0.0 )

for i in range ( num_steps ):

    x_dot, y_dot, z_dot = strangeAttractor( xs[i], ys[i], zs[i] )

    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)


# Plot
fig = plt.figure()
ax = fig.gca( projection='3d', adjustable='box' )

ax.plot( xs, ys, zs, lw=0.45 )
#ax.set_xlim(-40, 40)
#ax.set_ylim(-40, 40)
#ax.set_zlim(-100, 100)
ax.set_xlabel( "X Axis")
ax.set_ylabel( "Y Axis" )
ax.set_zlabel( "Z Axis" )
ax.set_title("Strange Attractor Type III")

plt.show()


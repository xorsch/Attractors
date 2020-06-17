
''' http://chaos-3d.e-monsite.com/pages/strange-attractor-type-i.html
'''

import numpy as np
import matplotlib.pyplot as plt
from numba import jit

s = 50.0

@jit(nopython=True)
def strangeAttractor(x, y, z, s=50.0, r=28.0, b=8.0/3.0):

    x_dot = 0.02 * y + 0.4 * x *( 0.2 - y**2 )                   
    y_dot = - x + s * z 
    z_dot = 10 * x -  0.1 * y  

    return x_dot, y_dot, z_dot

dt = 0.001
num_steps = 500000

# Need one more for the initial values
xs = np.empty( num_steps + 1 )
ys = np.empty( num_steps + 1 )
zs = np.empty( num_steps + 1 )

# Set initial values
xs[0], ys[0], zs[0] = ( 0.0, 1.0, 1.05 )

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):

    x_dot, y_dot, z_dot = strangeAttractor(xs[i], ys[i], zs[i])

    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)


# Plot
fig = plt.figure()
ax = fig.gca( projection='3d' )

ax.plot( xs, ys, zs, lw=0.35 )
#ax.set_xlabel( "X Axis")
#ax.set_ylabel( "Y Axis" )
#ax.set_zlabel( "Z Axis" )
ax.set_title("Strange Attractor Type I")

plt.show()

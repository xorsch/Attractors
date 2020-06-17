# https://en.wikipedia.org/wiki/R%C3%B6ssler_attractor
import numpy as np
import matplotlib.pyplot as plt

# A = 0.2, B = 0.2 y C =  5.7,
# A = 0.1, B = 0.1 y C = 14.0

dt = 0.0001
num_steps = 10000000

a, b, c = 0.1, 0.1, 12.0
rossler = np.zeros( (3,num_steps+1), dtype='float64' )
ts = np.arange( 1, num_steps+1)

rossler[0][0] = 10
rossler[1][0] = 10
rossler[2][0] = 10

for i in range (num_steps):

    rossler[0][i+1] = rossler[0][i] + ( (    -rossler[1][i] -     rossler[2][i]       ) * dt)
    rossler[1][i+1] = rossler[1][i] + ( (     rossler[0][i] + a * rossler[1][i]       ) * dt)
    rossler[2][i+1] = rossler[2][i] + ( ( b + rossler[2][i] *   ( rossler[0][i] - c ) ) * dt)


# Plot
fig, [ax1, ax2, ax3] = plt.subplots( 3, 1, sharex=True )
fig.suptitle( "Rossler Attractors " )
ax1.plot( ts, rossler[0], 'r,', lw=2 )
ax2.plot( rossler[1], 'g,', lw=2 )
ax3.plot( rossler[2], 'b,', lw=2 )

#ax1.set_title( 'x axis', loc='left' )
#ax2.set_title( 'y axis', loc='left' )
#ax3.set_title( 'z axis', loc='left' )

#ax1.grid( True )
#ax2.grid( True )
#ax3.grid( True )

# Setting x axis
#ax1.xaxis.set_major_locator( MultipleLocator(50000) )
#ax1.xaxis.set_major_formatter( FormatStrFormatter('%d') )
#ax1.xaxis.set_minor_locator( MultipleLocator(10000) )

# Setting y axis
#ax1.yaxis.set_major_locator( MultipleLocator(1 ) )
#ax1.xaxis.set_major_formatter( FormatStrFormatter('%d') )
#ax1.yaxis.set_minor_locator( MultipleLocator(.5) )

#ax2.yaxis.set_major_locator( MultipleLocator(1 ) )
#ax2.xaxis.set_major_formatter( FormatStrFormatter('%d') )
#ax2.yaxis.set_minor_locator( MultipleLocator(.5) )

#ax3.yaxis.set_major_locator( MultipleLocator(.05 ) )
#ax3.xaxis.set_major_formatter( FormatStrFormatter('%d') )
#ax3.yaxis.set_minor_locator( MultipleLocator(.025) )

plt.show()
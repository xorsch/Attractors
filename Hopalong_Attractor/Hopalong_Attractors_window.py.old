
import numpy as np
from numba import jit
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


@jit(nopython=True)
def Hopalong_create( size ):

    Hopalong = np.zeros( ( 2,size ) )

    return Hopalong


@jit(nopython=True)
def Hopalong_calc( hopalong, iterations, a, b, c ):


    for n in range ( 2,iterations ): 

        hopalong[0][n] =     hopalong[1][n-1] - 1 - np.sqrt( np.fabs(b * hopalong[0][n-1] - 1 - c) ) * np.sign( (hopalong[0][n-1]-1) ) 
        hopalong[1][n] = a - hopalong[0][n-1] - 1

    return hopalong

fig, ax = plt.subplots()
ax.axis('equal')
plt.subplots_adjust( left=0.15, bottom=0.4 )


var_a = 7.16878197155893
var_b = 8.43659746693447
var_c = 2.55983412731439
delta_f = 0.00000001
iterations = 1000000

hopalong = Hopalong_create( iterations )
g = Hopalong_calc( hopalong, iterations, var_a, var_b, var_c )
l, = plt.plot( g[0], g[1], ',', lw=0.2, alpha=0.1 )
ax.margins(x=0)

axcolor = 'lightblue'
ax_var_i = plt.axes([ 0.15, 0.175, 0.5, 0.0175 ], facecolor=axcolor)
ax_var_a = plt.axes([ 0.15, 0.150, 0.5, 0.0175 ], facecolor=axcolor)
ax_var_b = plt.axes([ 0.15, 0.125, 0.5, 0.0175 ], facecolor=axcolor)
ax_var_c = plt.axes([ 0.15, 0.100, 0.5, 0.0175 ], facecolor=axcolor)

s_var_i = Slider(ax_var_i, 'iter: ', 100000, 10000000, valinit=iterations, valstep=100, valfmt='%9i')
s_var_a = Slider(ax_var_a, 'a: ', -10, 10, valinit=var_a, valstep=delta_f, valfmt='%1.9f')
s_var_b = Slider(ax_var_b, 'b: ', -10, 10, valinit=var_b, valstep=delta_f, valfmt='%1.9f')
s_var_c = Slider(ax_var_c, 'c: ', -10, 10, valinit=var_c, valstep=delta_f, valfmt='%1.9f')

def update( val ):
    a    = s_var_a.val
    amp  = s_var_b.val
    amp2 = s_var_c.val
    iterations = int(s_var_i.val)

    hopalong = Hopalong_create( iterations )
    g = Hopalong_calc( hopalong, iterations, a, amp, amp2 )
    
    l.set_xdata( g[0] )
    l.set_ydata( g[1] )

    fig.canvas.draw_idle()


s_var_a.on_changed( update )
s_var_b.on_changed( update )
s_var_c.on_changed( update )
s_var_i.on_changed( update )

resetax = plt.axes( [0.8, 0.025, 0.1, 0.04] )
button = Button(resetax, 'Reset')


def reset(event):
    s_var_a.reset()
    s_var_b.reset()
    s_var_c.reset()
    s_var_i.reset()

button.on_clicked(reset)


plt.show()

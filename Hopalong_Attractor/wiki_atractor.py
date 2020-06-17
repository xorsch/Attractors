import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(state, t):
    x, y, z = state  # Desempaqueta el vector de estado
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivadas

state0 = [5.0, -5.0, 20.0]
state1 = [5.1, -4.9, 20.1]
t = np.arange(0.0, 30.0, 0.01)

states  = odeint(f, state0, t)
states2 = odeint(f, state1, t)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot( states[:, 0],   states[:, 1],  states[:, 2], lw=.65 )
ax.plot( states2[:, 0], states2[:, 1], states2[:, 2], lw=.65 )
plt.show()

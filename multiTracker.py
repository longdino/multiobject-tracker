import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D





def _update_plot(i, fig, scat):
    print(i)
    scat._offsets3d = ([0, i, i], [50, 20, 0], [100, 80, i])
    return scat


fig = plt.figure()

x = [0, 50, 100]
y = [0, 20, 80]
z = [0, 0, 0]

ax = fig.add_subplot(111, projection='3d')

scat = ax.scatter(x, y, z)

ax.set_xlim(0,100)
ax.set_ylim(0,100)
ax.set_zlim(0,100)

anim = animation.FuncAnimation(fig, _update_plot, fargs=(fig, scat), frames=100, interval=10)

plt.show()
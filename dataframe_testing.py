import pandas as pd
import matplotlib.animation as animation
import matplotlib;matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3


data=pd.read_excel(r'C:\Users\Hayoung\aggiechallenge\Multiobject-Tracker\MovingTrim3.xlsx')
# y0 = data.iloc[0, 0] #data.iloc is used to load specific cells from the dataframes created by pd.read_excel
# x0= data.iloc[0, 1]
# y1 = data.iloc[0, 2]
# x1= data.iloc[0, 3]
# y2 = data.iloc[0, 4]
# x2= data.iloc[0, 5]
# y3 = data.iloc[0, 6]
# x3= data.iloc[0, 7]
# z0 = data.iloc[0, 8]
# z1 = data.iloc[0, 9]
# z2 = data.iloc[0, 10]
# z3 = data.iloc[0, 11]
x = data.iloc[0,0]
y = data.iloc[0,1]
z = data.iloc[0,2]



def _update_plot(i, fig, scat):
    # y0 = data.iloc[i, 0] #grabs the next data point in a given column with each iteration
    # x0 = data.iloc[i, 1]
    # y1 = data.iloc[i, 2]
    # x1 = data.iloc[i, 3]
    # y2 = data.iloc[i, 4]
    # x2 = data.iloc[i, 5]
    # y3 = data.iloc[i, 6]
    # x3 = data.iloc[i, 7]
    # z0 = data.iloc[i, 8]
    # z1 = data.iloc[i, 9]
    # z2 = data.iloc[i, 10]
    # z3 = data.iloc[i, 11]

    # x = [x0, x1, x2, x3]
    # y = [y0, y1, y2, y3]
    # z = [z0, z1, z2, z3]
    x = data.iloc[i,0]
    y = data.iloc[i,1]
    z = data.iloc[i,2]

    scat._offsets3d = (x, y, z) #updates the scatterplot with the latest data set

    return scat


fig = plt.figure()
# x = [x0, x1, x2, x3]
# y = [y0, y1, y2, y3]
# z = [z0, z1, z2, z3]

ax = fig.add_subplot(111, projection='3d')
ax.grid(True, linestyle='-', color='0.75')
ax.set_xlim3d([0, 1500])
ax.set_ylim3d([0, 1500])
ax.set_zlim3d([0, 1500])
scat = ax.scatter(x, y, z, c=x)
scat.set_alpha(0.8)

anim = matplotlib.animation.FuncAnimation(fig, _update_plot, fargs=(fig, scat), frames=500, interval=20, blit=False)

plt.show()

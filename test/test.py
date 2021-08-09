import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = [1, 2, 3, 4, 5, 6, 7, 8, 9]
xline = [1, 2, 3, 4, 5, 6, 7, 8, 9]
yline = [1, 2, 3, 4, 1, 6, 7, 8, 9]
ax.plot3D(xline, yline, zline)

# Data for three-dimensional scattered points
# zdata = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ydata = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# zdata = []
# xdata = []
# ydata = []
# ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

fig.show()

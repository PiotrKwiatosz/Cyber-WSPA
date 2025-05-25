import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generowanie losowych punktow
num_points = 100
x = np.random.random(num_points) * 10
y = np.random.random(num_points) * 10
z = np.random.random(num_points) * 10

# Tworzenie figury
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Rysowanie punktow
ax.scatter(x, y, z, c='red', marker='o')

# Etykiety osi
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()
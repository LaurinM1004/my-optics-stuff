from classes import Ray,Lens
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from typing import cast
from mpl_toolkits.mplot3d.art3d import Line3D

num_rays = 10
rays = [Ray([x, 0, 0], [0, 0, 1]) for x in np.linspace(-0.01, 0.01, num_rays)]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlim(-0.02, 0.02)
ax.set_ylim(-0.02, 0.02)
ax.set_zlim(0, 0.1)
ax.set_xlabel("X [m]")
ax.set_ylabel("Y [m]")
ax.set_zlabel("Z [m]")

lines = [cast(Line3D, ax.plot([], [], [])[0]) for _ in rays]


def init():
    for line in lines:
        line.set_data([], [])
        line.set_3d_properties([])
    return lines

def update(frame):
    for i, ray in enumerate(rays):
        ray.propagate(0.005)  # Schrittweite
        path = np.array(ray.path)
        # Option B: use the combined 3D helper (alternative)
        lines[i].set_data_3d(path[:, 0], path[:, 1], path[:, 2])
    return lines

ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=False, interval=50)
plt.show()
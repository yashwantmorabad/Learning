import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Define our vectors
origin = [0, 0, 0]
v = np.array([2, 1, 0])      # On the floor
w = np.array([1, 4, 0])      # On the floor
x = np.array([1, 2, 10])    # Slanted up into the air
p = np.cross(v, w)           # The cross product (straight up)
print(np.dot(p, x))          # The dot product (slanted up)

# Combine vectors for plotting
vectors = np.array([v, w, p, x])
colors = ['blue', 'green', 'red', 'purple']
labels = ['Vector v (floor)', 'Vector w (floor)', 'Cross Product p (straight up)', 'Vector x (slanted)']

# Plot each vector
for i in range(4):
    ax.quiver(*origin, *vectors[i], color=colors[i], arrow_length_ratio=0.1, linewidth=2, label=labels[i])

# Formatting the plot
ax.set_xlim([0, 3])
ax.set_ylim([0, 5])
ax.set_zlim([0, 8])
ax.set_xlabel('X axis (Floor)')
ax.set_ylabel('Y axis (Floor)')
ax.set_zlabel('Z axis (Height)')
ax.set_title('Visualizing Volume, Cross Product, and Vector x')
ax.legend()

plt.show()
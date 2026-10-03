import matplotlib.pyplot as plt
import numpy as np

# Define vectors
A = np.array([4, 0])
B = np.array([2, 2])

# Calculate dot product
dot_product = np.dot(A, B)

# Plotting
plt.figure()
plt.grid()
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Draw vectors
plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector A [4,0]')
plt.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector B [2,2]')

# Draw the projection (shadow) of B onto A
plt.plot([B[0], B[0]], [B[1], 0], 'k--', label='Shadow of B on A')
plt.quiver(0, 0, 2, 0, angles='xy', scale_units='xy', scale=1, color='green', label='Projection (Length=2)')

plt.xlim(-1, 6)
plt.ylim(-1, 4)
plt.title(f"Dot Product Visualization (A · B = {dot_product})")
plt.legend()
plt.show()
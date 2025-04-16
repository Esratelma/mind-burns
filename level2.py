import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Magnitudes
A_mag = 12
B_mag = 5

# Vector A (fixed along x-axis)
A = np.array([A_mag, 0])

# Angle to reach (pi/2)
theta_final = np.pi / 2

# Set up plot
fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(0, 15)
ax.set_aspect('equal')
ax.grid()

vectorA = None
vectorB = None
vectorC = None
text = None

def init():
    global vectorA, vectorB, vectorC, text
    vectorA = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='r', label='A')
    vectorB = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='g', label='B')
    vectorC = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='b', label='C = A + B')
    text = ax.text(1, 13, '', fontsize=12)
    ax.legend()
    return vectorA, vectorB, vectorC, text

def update(frame):
    global vectorA, vectorB, vectorC, text
    ax.clear()
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 15)
    ax.set_aspect('equal')
    ax.grid()

    theta = frame * (theta_final / 60)  # Smooth step up to pi/2

    # Vector A is fixed
    A = np.array([A_mag, 0])
    # Vector B rotates from 0 to pi/2
    B = np.array([B_mag * np.cos(theta), B_mag * np.sin(theta)])
    # Vector C = A + B
    C = A + B

    # Draw vectors
    ax.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='r', label='A')
    ax.quiver(A[0], A[1], B[0], B[1], angles='xy', scale_units='xy', scale=1, color='g', label='B')
    ax.quiver(0, 0, C[0], C[1], angles='xy', scale_units='xy', scale=1, color='b', label='C = A + B')

    # Angle in degrees
    angle_deg = np.degrees(theta)
    ax.set_title(f'Angle between A and B: {angle_deg:.1f}°')

    ax.legend()
    return ax

ani = animation.FuncAnimation(fig, update, frames=61, init_func=init, interval=100, blit=False)
plt.show()

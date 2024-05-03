# Bouncing circles
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches


class Circle:
    def __init__(self, x_min, x_max, y_min, y_max, s, r_min, r_max, d_rad):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.w = x_max - x_min
        self.h = y_max - y_min
        self.r = np.random.rand() * self.w / 2 + self.w * 0.05  # Radius of a circle
        # Point of a circle
        self.p = np.array([np.random.rand() * self.w - self.w / 2, np.random.rand() * self.h - self.h / 2])
        self.theta = np.random.rand() * 2. * math.pi  # Angle of vector
        self.v = s * np.array([math.cos(self.theta), math.sin(self.theta)])  # Vector of a circle
        self.r_min = r_min
        self.r_max = r_max
        self.d_rad = d_rad

    def move_and_change_radius(self):
        self.p = self.p + self.v  # Update position
        # Reverse vector if out out of range
        if self.p[0] > self.x_max or self.p[0] < self.x_min:
            self.v = np.dot(reverse_h, self.v)
        if self.p[1] > self.y_max or self.p[1] < self.y_min:
            self.v = np.dot(reverse_v, self.v)
        self.r = self.r + self.d_rad  # Update radius
        if self.r > self.r_max or self.r < self.r_min:
            self.d_rad = -self.d_rad

    def get_point(self):
        return self.p

    def get_radius(self):
        return self.r


def set_axis():
    ax.set_title("Bouncing circles")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect("equal")
    ax.grid()


def update(f):
    ax.cla()  # Clear ax
    set_axis()
    ax.text(x_min, y_max * 0.9, "Step=" + str(f))

    global circles
    for obj in circles:
        obj.move_and_change_radius()
        p = obj.get_point()
        r = obj.get_radius()
        circle_draw = patches.Circle(xy=p, radius=r, fill=False)
        ax.add_patch(circle_draw)


# Global variables
x_min = -10.
x_max = 10.
y_min = -10.
y_max = 10.
r_max = 10.
r_min = 1.
drad = 0.1  # Step to change radius
sclr = 0.5  # Scalar of velocity
reverse_h = np.array([[-1, 0], [0, 1]])  # Matrix of horizontal reverse
reverse_v = np.array([[1, 0], [0, -1]])  # Matrix of vertical reverse

# Generate circles
circles = []
for i in range(10):
    circle = Circle(x_min, x_max, y_min, y_max, sclr, r_min, r_max, drad)
    circles.append(circle)

# Generate figure and axes
fig = plt.figure()
ax = fig.add_subplot(111)

# Draw animation
set_axis()
anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
plt.show()

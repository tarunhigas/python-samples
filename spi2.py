import math
import matplotlib.pyplot as plt


def spirograph(R=120, r=55, d=65, color="purple"):
    gcd_val = math.gcd(int(R), int(r))
    steps = 360 * (r // gcd_val)

    x_points = []
    y_points = []

    for angle in range(0, steps):
        theta = math.radians(angle)
        x = (R - r) * math.cos(theta) + d * math.cos((R - r) / r * theta)
        y = (R - r) * math.sin(theta) - d * math.sin((R - r) / r * theta)
        x_points.append(x)
        y_points.append(y)

    plt.figure(figsize=(6, 6), facecolor="white")
    plt.plot(x_points, y_points, color=color, linewidth=0.8)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


spirograph(R=120, r=55, d=65)

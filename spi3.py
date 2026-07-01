import math


def spirograph(R=120, r=55, d=65, width=80, height=40):
    points = set()

    gcd_val = math.gcd(int(R), int(r))
    steps = 360 * (r // gcd_val)

    raw = []
    for angle in range(0, steps):
        theta = math.radians(angle)
        x = (R - r) * math.cos(theta) + d * math.cos((R - r) / r * theta)
        y = (R - r) * math.sin(theta) - d * math.sin((R - r) / r * theta)
        raw.append((x, y))

    min_x = min(p[0] for p in raw)
    max_x = max(p[0] for p in raw)
    min_y = min(p[1] for p in raw)
    max_y = max(p[1] for p in raw)

    for x, y in raw:
        col = int((x - min_x) / (max_x - min_x) * (width - 1))
        row = int((y - min_y) / (max_y - min_y) * (height - 1))
        points.add((row, col))

    for row in range(height - 1, -1, -1):
        line = ""
        for col in range(width):
            line += "*" if (row, col) in points else " "
        print(line)


spirograph()

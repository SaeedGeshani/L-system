import matplotlib.pyplot as plt
import random

def barnsley_fern(iterations):
    x, y = 0, 0
    xs, ys = [], []
    for _ in range(iterations):
        r = random.random()
        if r < 0.01:
            x, y = 0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        xs.append(x)
        ys.append(y)
    return xs, ys

xs, ys = barnsley_fern(100000)
plt.scatter(xs, ys, s=0.1, color='green', marker='.')
plt.show()
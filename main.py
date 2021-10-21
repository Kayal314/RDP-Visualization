import time
import numpy as np
import math
from matplotlib import pyplot as plt
from tools import douglas_peucker

x_coordinates = np.linspace(0, 5, 1000)


def func(x: float) -> float:
    return math.e ** (-x) * math.cos(2 * math.pi * x)


def get_points_separated(point_list):
    return [point[0] for point in point_list], [point[1] for point in point_list]


y_coordinates = [func(x) for x in x_coordinates]

points = [(x, func(x)) for x in x_coordinates]

x_data = []
y_data = []

plt.show()

axes = plt.gca()
axes.set_xlim(0, 5)
axes.set_ylim(-1, +1)
line, = axes.plot(x_data, y_data, marker='x', linestyle='dashed', color='red')
line_original, = axes.plot(x_data, y_data,  color='#c0c6cf')

for epsilon in np.linspace(0.0, 0.8, 400):
    new_points = douglas_peucker(points, 0, len(points) - 1, epsilon)
    print(f'epsilon = {epsilon}, n = {len(new_points)}')
    x_data, y_data = get_points_separated(new_points)
    # line_original.set_xdata(x_coordinates)  to show original set along with the calculated set
    # line_original.set_ydata(y_coordinates)  remove the comment tags
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    plt.pause(1e-17)
    time.sleep(0.5)

plt.show()

import math


def perpendicular_dist(point: tuple, line_start_point: tuple, line_end_point: tuple) -> float:
    m = (line_end_point[1] - line_start_point[1]) / (line_end_point[0] - line_start_point[0])
    num = point[1] - m * point[0] + m * line_start_point[0] - line_start_point[1]
    den = (1 + m ** 2) ** 0.5
    return math.fabs(num / den)


def douglas_peucker(points: list, start: int, end: int, epsilon: float) -> list:
    max_dist = -1
    index = 0
    for i in range(start + 1, end):  # exclude the first and last point
        dist = perpendicular_dist(points[i], points[start], points[end])
        if dist > max_dist:
            index = i
            max_dist = dist

    if max_dist > epsilon:
        # recursively call the function
        result_left = douglas_peucker(points, start, index, epsilon)
        result_right = douglas_peucker(points, index, end, epsilon)
        result = result_left + result_right

    else:
        result = [points[start], points[end]]

    return result

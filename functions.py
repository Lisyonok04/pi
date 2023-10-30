import sys
import time
import random
import concurrent.futures


def is_inside_circle(radius: float, x: float, y: float) -> bool:
    if (x**2 + y**2) <= radius**2:
        return True
    return False


def concurrent_count_pi(points: int) -> float:
    x = []
    y = []
    in_circle: int = 0
    radius: int = 10
    for i in range(points):
        x.append(random.uniform(-1 * radius, 1 * radius))
        y.append(random.uniform(-1 * radius, 1 * radius))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        res = [
            executor.submit(is_inside_circle, radius, xi, yi) for xi, yi in zip(x, y)
        ]
        for future in concurrent.futures.as_completed(res):
            in_circle += int(future.result())
    return float(in_circle) / points * 4


def main():

    points = int(sys.argv[1])
    t0 = time.time()
    res = concurrent_count_pi(points)
    print(f"Значение числа пи = {res}, время выполнения программы = {time.time() - t0}")
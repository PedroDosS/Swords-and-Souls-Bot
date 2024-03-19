import time
import math
import time
import sys

# Used to nicely format time
def time_since(t):
    time_ellapsed = time.time() - t
    time_ellapsed_formatted = time.strftime('%H:%M:%S', time.gmtime(time_ellapsed))
    return f'{time_ellapsed_formatted} ({time_ellapsed} ms)'

# Partitions the coordinates as part of the quicksort algorithm
def partition(l, r, coords, distances):
    pivot, ptr = distances[r], l
    for i in range(l, r):
        if distances[i] <= pivot:
            distances[i], distances[ptr] = distances[ptr], distances[i]
            coords[i], coords[ptr] = coords[ptr], coords[i]
            ptr += 1
    distances[ptr], distances[r] = distances[r], distances[ptr]
    coords[ptr], coords[r] = coords[r], coords[ptr]

    return ptr

# Sorts the coordinates around the player in closet to farthest order
def quicksort(l, r, coords, distances):
    if len(distances) == 1:
        return distances
    if l < r:
        pi = partition(l, r, coords, distances)
        quicksort(l, pi-1, coords, distances)
        quicksort(pi+1, r, coords, distances)
    return coords, distances

# Writes the ordered coordinates to a text file to avoid needing to recompute them
def save_coords(coords, check_size, path):
    with open(path, 'w') as file:
        file.write(f'{check_size}\n')
        file.write(f'{coords}\n')

# Finds the closest coordinates to an origin
def get_spiral_coords(origin, check_size, path, min_radius=0, max_radius=1000):
    sys.setrecursionlimit(100000)

    x_coords = range(check_size[0], check_size[2])
    y_coords = range(check_size[1], check_size[3])

    distances = []
    coords = []

    start = time.time()

    # Calculates the distance from each coordinate to the origin
    for x_coord in x_coords:
        for y_coord in y_coords:
            coord = [x_coord, y_coord]
            dist = math.dist(origin, coord)
            if min_radius <= dist <= max_radius:
                distances.append(dist)
                coords.append(coord)

    print(f'Generating coords took {time_since(start)}')

    # Sorts the coordinates in closest to furthest order
    start = time.time()
    coords, distances = quicksort(0, len(distances)-1, coords, distances)
    print(f'Sorting the coords took {time_since(start)}')

    start = time.time()
    save_coords(coords, check_size, path)
    print(f'Saving took {time_since(start)}')

    return coords

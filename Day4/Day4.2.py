import numpy as np
from scipy.signal import convolve2d

puzzle = [line.strip() for line in open("Data.csv").readlines()]

grid = np.array([[ord(char) for char in line] for line in puzzle])

x_mas = np.array([[1 / ord('M'), 0, 1 / ord('S')],
                  [0, 1 / ord('A'), 0],
                  [1 / ord('M'), 0, 1 / ord('S')]])

rotations = [np.rot90(x_mas, i) for i in range(4)]

total = 0
for rot in rotations:
    conv = convolve2d(grid, rot, mode='valid')
    total += np.count_nonzero(conv == 5)
print(total)
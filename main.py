import math as m
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def initCoords(resolution):
	grid = []
	for x in range(resolution):
		j = 0
		array = []
		while j < resolution:
			array.append((x * resolution) + j)
			j = j + 1
		grid.append(array)
	coordinates = np.array(grid)

	return coordinates.transpose()


def main():
	# coordRange = int(input("Please enter the range of the simulation: "))
	coordRange = 8
	coords = initCoords(coordRange)

	# plt.imshow(coords,cmap="coolwarm")
	# plt.title("Plot 2D array")
	# plt.colorbar()
	# plt.show()
main()
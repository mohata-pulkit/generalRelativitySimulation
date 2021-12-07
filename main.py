import math as m
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def initCoords(resolution):
	grid = []
	for x in range(resolution):
		array = []
		for y in range(resolution):
			array.append((x * resolution) + y)
		grid.append(array)
	coordinates = np.array(grid)

	return coordinates


def main():
	# coordRange = int(input("Please enter the range of the simulation: "))
	coordRange = 256
	coords = initCoords(coordRange)

	print(coords)

	# plt.imshow(coords,cmap="coolwarm")
	# plt.title("Plot 2D array")
	# plt.colorbar()
	# plt.show()
main()
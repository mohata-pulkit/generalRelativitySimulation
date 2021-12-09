import math as m
import time as t
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

def addPointMass(coords, mass, position):
	G = 6.67430 * (10**(-11))

	newCoords = []

	for x in coords.tolist():
		array = []
		for y in x:
			if((m.sqrt((((y % len(x)) - position[0])**2) + (((m.floor(y / len(x)) - position[1])**2)))) != 0):
				array.append((G * mass * -1)/(m.sqrt((((y % len(x)) - position[0])**2) + (((m.floor(y / len(x)) - position[1])**2)))))
			else:
				array.append((G * mass * -1))
		newCoords.append(array)

	newCoords = np.array(newCoords)
	return newCoords

def main():
	# coordRange = int(input("Please enter the range of the simulation: "))
	coordRange = 256
	coords = initCoords(coordRange)

	coords = addPointMass(coords, 5e10, [128, 128])

	plt.imshow(coords)
	plt.title("Plot 2D array")
	plt.colorbar()
	plt.show()
main()
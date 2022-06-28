import math as m
import time as t
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def initCoords(x, y):
	coords = np.zeros([x, y])
	return coords

def addPointMass(field, mass, position):
	G = 1

	newField = field
	
	x = 0
	while x < len(newField):
		y = 0
		while y < len(newField[0]):
			if x == position[0] and y == position[1]:
				newField[x, y] = newField[x, y] + (G * mass * -1)
			else:
				newField[x, y] = newField[x, y] + ((G * mass * -1) / ((x - position[0])**2 + (y - position[1])**2))
			y = y + 1
		x = x + 1
	return newField

def main():
	range = 128
	field = initCoords(range, range)
	field = addPointMass(field, 5e24, [31, 31])
	field = addPointMass(field, 5e23, [95, 95])

	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')

	x = np.linspace(0, range, range)
	y = np.linspace(0, range, range)

	X, Y = np.meshgrid(x, y)

	ax.plot_wireframe(X, Y, field)

	# x = 0
	# while x < range:
	# 	y = 0
	# 	while y < range:
	# 		ax.scatter(x, y, field[x, y])
	# 		y = y + 1
	# 	x = x + 1

	plt.show()

main()
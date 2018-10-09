#!/usr/bin/python
from numpy import *

def run():
	# reaching the dataset
	points = genfromtxt("data.csv", delimiter=",")
	#initializing hyperparameters
	learning_rate = 0.0001
	initial_b = 5.5 # initial y-intercept guess
	initial_m = 5.5 # initial slope guess
	num_iterations = 100000
	print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, error_with_given_points(initial_m,initial_b,points))
	
	print "Running..."
	
	[m, b] = gradient_descent_runner(initial_m, initial_b, points, num_iterations, learning_rate)
	
	print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, error_with_given_points(m,b,points))





def error_with_given_points(m, b, points):
	totalError = 0

	for i in range(len(points)):
		x = points[i, 0]
		y = points[i, 1]

		totalError += (y - (m*x + b)) ** 2

	return totalError/float(len(points))

def gradient_descent_runner(current_m, current_b, points, max_iteration, learning_rate):
	m = current_m
	b = current_b
	for i in range(max_iteration):
		m, b = step_gradient(m, b, points, learning_rate)

	return m, b

def step_gradient(m, b, points, learning_rate):
	gradient_m = 0
	gradient_b = 0
	N = float(len(points))

	for i in range(len(points)):

		x = points[i,0]
		y = points[i,1]

		gradient_b += -(2/N) * (y - ((m * x) + b))
		gradient_m += -(2/N) * x * (y - ((m * x) + b))

	new_m = m - (gradient_m * learning_rate)
	new_b = b - (gradient_b * learning_rate)

	return new_m, new_b



if __name__ == "__main__":
	run();

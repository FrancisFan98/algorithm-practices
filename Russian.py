#!/usr/bin/python

def russian(a,b):
	x = a
	y = b
	z = 0
	while x > 0:
		if x % 2 == 1: 
			z += y
		x = x >> 1
		y = y << 1
	return z
	
def times(a,b):
	x = a
	y = b
	z = 0
	while x > 0:
		z += y
		x -= 1
	return z
	
print russian(2**30, 2**30)
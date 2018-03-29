#!/usr/bin/python


import time 
def decorater(fn): 
	cache = {} 
	def _d(n): 
		if n in cache: 
			return cache[n]  
		else: 
			cache[n] = fn(n)
			return cache[n]	 
	return _d

def timer(fn): 
	def _d(*n):
		a = time.time() 
		result = fn(*n)
		b = time.time()
		print  b-a 
		return result
	return _d	 

@decorater
@timer
def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

@timer 
def sadv():
	print "A" 
	
sadv() 


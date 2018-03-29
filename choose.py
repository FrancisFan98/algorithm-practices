#!/usr/bin/python
import random

def choose(n1,n2):
	a = range(n2)
	b = set()
	while len(b) != n1:
		b.add(random.randint(0, len(a)-1))
	#print a	
	print b
	a = [a[x] for x in b]
	return a 	
	
print choose(2, 5)
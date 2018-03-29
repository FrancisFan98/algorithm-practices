#!/usr/bin/python

def nQueen(n):
	# solve caller
	if n <= 3:
		return "Incorrect input : # of Queen has to be more than 3"
		 
	positions = []
	for i in range(n):
		positions.append([-1,-1])
	solveNQueen(n, 0, positions)
	return positions
	


def solveNQueen(n, row, positions):
	
	if(n == row):
		return True
		
	for col in range(n):
		foundSafe = True
		
		for Q in range(row):
			if attack(positions[Q], (row, col)):
				foundSafe = False
				break
		if (foundSafe):
			positions[row] = (row, col)
			if(solveNQueen(n, row + 1, positions)):
				return True
				
	return False					

def attack(p1, p2):
	if p1 == (-1, -1) or p2 == (-1, -1):
		return False
	if(p1[0] == p2[0] or p1[1] == p2[1] or (p1[0] + p1[1]) == (p2[0] + p2[1]) or (p1[0] - p1[1]) == (p2[0] - p2[1])):
		return True
	return False	
	
print nQueen(3)
	
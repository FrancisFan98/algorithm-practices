#!/usr/bin/python
import random, math, collections


def shuffle(deck):
	length = len(deck)
	for e in range(0, length-1):
		swap(deck, e, random.randrange(e, length))

def swap(deck, i, j):
	deck[i], deck[j] = deck[j], deck[i]
	
def test_shuffle(shuffler, deck, n = 100000):
	ex = (n*1.)/math.factorial(len(deck))
	result = collections.defaultdict(int)
	for e in range(0, n):
		Input = list(deck)
		shuffler(Input)
		result["".join(Input)] += 1
	
	ok = all([(0.9*ex) <= result[item] <= (1.1*ex) for item in result])	
	for item in result:
		print "%s%s%4.2f%s" % (item, " : " , result[item]*100./100000, "%")
	print ("ok" if ok else "***BAD***")



	
	
def allMax(hands, key = None):
	
	result = []
	current_max = None
	
	key = key or (lambda x:x)
	
	hand_max = None
	
	for hand in hands:
		if key(hand) > current_max:
			result = []
			current_max = key(hand)
			hand_max = hand
		if key(hand) == current_max:	
			result.append(key(hand))
	
	return result, hand_max



def hand_ranks(hand):
	ranks = ["--23456789TJQKA".index(r) for r,s  in hand]

	return sorted(ranks, reverse = True)
	
	
def kind(n, ranks):
	value = None
	for rank in ranks:
		if ranks.count(rank) == n:
			return rank
			
	return False
	
def two_pair(ranks):
	first = kind(2, ranks)
	second = kind(2, list(reversed(ranks)))

	if first != second and first:
		return (first, second)
	return False		


def straight(ranks):
	return  (len(set(ranks)) == 5 and ranks[0] - ranks[-1] == 4)


def flush(hand):
	color = [s for r,s in hand]
	return len(set(color)) == 1

def card_rank(hand):
	ranks = hand_ranks(hand)
	
	if straight(ranks) and flush(hand):
		return (9, ranks[0])
	elif kind(4, ranks):
		return (8, kind(4, ranks), kind(1, ranks))
	elif kind(3, ranks) and kind(2, ranks):
		return (7, kind(3, ranks), kind(2, ranks))
	elif flush(hand):
		return (6, hand)
	elif straight(ranks):
		return (5, ranks[0])
	elif kind(3, ranks):
		return (4, kind(3, ranks), kind(1, ranks), kind(1, list(reversed(ranks))))
	elif two_pair(ranks):
		return (3, two_pair(ranks), kind(1, ranks))
	elif kind(2, ranks):
		return (2, ranks)
	else:
		return (1, ranks)
	
	
deck = [r + s for r in "23456789TJQKA" for s in "shdc"]
shuffle(deck)

def deal(deck, number, n = 5):
	output = [] 
	
	for i in range(number):
		output.append(deck[i*n:n*(i+1)])
	return output

hands = deal(deck, 5)

def poker(hands):
		
		return allMax(hands, key = card_rank)

print hands
print poker(hands)








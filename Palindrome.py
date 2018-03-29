

def isPalindrome(text):
	if len(text) == 1 and len(text)==0: 
		return True
	mid = len(text)/2
	return text[:mid] == text[:mid:-1]

def longest_subpalindrome_slice(text):
	"Return (i, j) such that text[i:j] is the longest palindrome in text."
	# Your code here
	longest = ""
	longPosition = None
	text = text.lower()
	if len(text) == 0:
		return (0,0)
	for e in range(len(text)):
		moves = 0

		while e-moves >= 0 and e+moves+1 <= len(text) and isPalindrome(text[e-moves:e+moves+1]):
			if len(text[e-moves: e+moves+1]) > len(longest):
				longest = text[e-moves: e+moves+1]
				longPosition = (e-moves, e+moves)
			moves += 1   
			 
	print longPosition
	return longPosition         
	

print longest_subpalindrome_slice("tattarrattat")

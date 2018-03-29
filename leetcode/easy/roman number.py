#!/usr/bin/python

class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		rs = 0
		cache = {"I" : 1, "V":5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
		allChars = "MDCLXVI"
		
		for i in range(len(s)):
			for e in range(len(allChars)):
				if s[i] == allChars[e]:
					rs += cache[allChars[e]]
					break
				else:
					try:
						if s[i+1] == allChars[e]:
							rs = rs - cache[s[i]]
							break
					except:
						pass		
		return rs
		
a = Solution()
print a.romanToInt("MCDLXXVI")
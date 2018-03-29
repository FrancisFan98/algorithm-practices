#!/usr/bin/python

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		start = maxLength = 0
		usedChars = {}

		for i in range(len(s)):
			if s[i] in usedChars and start <= usedChars[s[i]]:
				start = usedChars[s[i]] + 1
			else:
				maxLength = max(maxLength, i - start +1)
				
			usedChars[s[i]] = i
		return maxLength

		
a = Solution()
print a.lengthOfLongestSubstring("ababc")
print a.lengthOfLongestSubstring("abcabcbb")
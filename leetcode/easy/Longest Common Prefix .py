class Solution(object):
	 def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if not strs:
			return ""
		
		shortest = min(strs, key = len)
		if not shortest:
			return ""
		
		for i in range(len(shortest)):
			print shortest
			group = [s[:i+1] for s in strs]
			
			if len(set(group)) != 1:
				return shortest[:i]
			
		return shortest
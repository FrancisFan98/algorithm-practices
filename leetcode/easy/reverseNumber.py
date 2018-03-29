#!/usr/bin/python

class Solution(object):
	
	def res(self,x):
		return "".join([i for i in reversed(str(x))])

	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""

		
		if x < 0:
			rt = int("-" + Solution.res(self,str(x)[1:]))
		
		else: 
			
			rt = int(Solution.res(self,x)) 

		return rt if (-2**32)/2 < rt < (2**32)/2 else 0
		

a = Solution()

print a.reverse(1512)

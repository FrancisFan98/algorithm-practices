# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def isEmpty(self, node):
		return node.next == None
	
	def findAllNums(self, node):
		rs = []
		while True:
			rs.append(str(node.val))
			if Solution.isEmpty(self,node):
				return rs
			else:
				node = node.next
		
		
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		Top = None
		nums1 = "".join(Solution.findAllNums(self, l1)[::-1])
		nums2 = "".join(Solution.findAllNums(self, l2)[::-1])
		answer = list(str(int(nums1)+int(nums2)))
		print answer
		for i in answer:
			cur = ListNode(int(i))
			cur.next = Top
			Top = cur
		return Top
				
				
					
					
					
		
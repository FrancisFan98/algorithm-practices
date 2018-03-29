#!/usr/bin/python

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):

	def addTwoNumbers(self, l1, l2):
		top = cur = ListNode(0)
		carry = 0
		print top is cur
		while(carry or l1 or l2):
			v1 = v2 = 0
			if l1:
				v1 = l1.val
				l1 = l1.next
			if l2:
				v2 = l2.val
				l2 = l2.next
			
			carry, remainder = divmod(v1+v2+carry, 10)
			
			cur.next = ListNode(remainder)
			cur = cur.next
			
		return top.next
		

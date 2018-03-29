#!/usr/bin/python

def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	for i in range(len(nums)):
		n = target - nums[i]
		if n in nums and n == nums[i]:
			first = nums.index(n)
			second = len(nums) - 1 - list(reversed(nums)).index(n)
			if first != second:
				return [first, second]
		elif n in nums:
			return i, nums.index(n)

print twoSum([3,2,4], 6)
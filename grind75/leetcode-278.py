

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
	def firstBadVersion(self, n: int) -> int:
		result = 1
		start, end = 1, n
		while start <= end:
			mid = (start + end) // 2
			if isBadVersion(mid) == False:
				start = mid + 1
			else:
				end = mid - 1
				result = mid
		return result
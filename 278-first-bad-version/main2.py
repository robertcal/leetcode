# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        min, max = 1, n  # min should start from 1

        while min < max:  # Change the condition to min < max
            mid = (min + max) // 2
            if isBadVersion(mid):
                max = mid  # Narrow the range from the right
            else:
                min = mid + 1  # Narrow the range from the left

        return min  # min will be the first bad version
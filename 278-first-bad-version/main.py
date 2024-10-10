# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # solved this on my own
    def firstBadVersion(self, n: int) -> int:
        min, max = 0, n

        while min + 1 < max:
            mid = (min + max) // 2
            if isBadVersion(mid):
                max = mid
            else:
                min = mid

        return max
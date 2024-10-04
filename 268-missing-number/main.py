class Solution:
    # solved this on my own
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        sum = int(n * (n + 1) / 2)

        for num in nums:
            sum -= num

        return sum
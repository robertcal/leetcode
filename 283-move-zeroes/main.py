class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # solved this on my own
        length = len(nums)
        cur = 0
        for i in range(length):
            if nums[cur] == 0:
                nums.pop(cur)
                nums.append(0)
            else:
                cur += 1

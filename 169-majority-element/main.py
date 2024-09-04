class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for n in nums:
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1

            if dict[n] > len(nums) // 2:
                return n
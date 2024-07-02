class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} # value: index
        for i, v in enumerate(nums):
            diff = target - v
            if diff in dict:
                return [dict[diff], i]

            dict[v] = i
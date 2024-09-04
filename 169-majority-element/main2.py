class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = defaultdict(int)
        border = len(nums) // 2
        for n in nums:
            count_dict[n] += 1

            if count_dict[n] > border:
                return n
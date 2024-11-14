class Solution:
    # solved this on my own
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, cur):
            if len(nums) == 0:
                res.append(cur)
                return

            for i in nums:
                cur.append(i)
                newNums = nums.copy()
                newNums.remove(i)
                dfs(newNums, cur.copy())
                cur.remove(i)

        dfs(nums, [])

        return res
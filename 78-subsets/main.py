class Solution:
    # solved this on my own
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)

        def rec(i, cur):
            if i > length - 1:
                res.append(cur)
                return

            rec(i + 1, cur.copy())
            cur.append(nums[i])
            rec(i + 1, cur)

        rec(0, [])

        return res
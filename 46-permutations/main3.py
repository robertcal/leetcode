class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur[:])  # 結果を保存する時のみコピー
                return

            for i in range(len(nums)):
                if nums[i] in cur:
                    continue  # すでに使われた要素をスキップ

                cur.append(nums[i])
                dfs(cur)
                cur.pop()  # 元に戻す（バックトラッキング）

        dfs([])
        return res
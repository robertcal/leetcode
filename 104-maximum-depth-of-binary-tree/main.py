# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # solved it on my own

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = self.dfs(root, 0)

        return ans

    def dfs(self, root: Optional[TreeNode], count: int):
        if root is None:
            return count

        count += 1

        return max(self.dfs(root.left, count), self.dfs(root.right, count))

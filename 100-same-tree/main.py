# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solved it on my own
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.ans = True

        def dfs(p, q):
            if not p and not q:
                return

            if (not p and q) or (p and not q):
                self.ans = False
                return

            if p.val != q.val:
                self.ans = False
                return

            dfs(p.left, q.left)
            dfs(p.right, q.right)

        dfs(p, q)
        return self.ans
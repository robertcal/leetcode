# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative dfs
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = []
        stack.append([root, 1])

        ans = 1

        while stack:
            # current, depth = stack.pop()とも書ける
            current = stack.pop()

            ans = max(ans, current[1])

            if current[0].left:
                stack.append([current[0].left, current[1] + 1])

            if current[0].right:
                stack.append([current[0].right, current[1] + 1])

        return ans

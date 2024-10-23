# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # solved this on my own
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        q.append(root)

        res = []
        while q:
            l = len(q)

            level = []
            for i in range(l):
                cur = q.pop(0)

                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
                    level.append(cur.val)

            if level:
                res.append(level)

        return res
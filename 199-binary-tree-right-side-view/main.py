# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # solved this on my own
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()

        if not root:
            return res

        q.append(root)

        while q:
            length = len(q)
            for i in range(length):
                target = q.popleft()
                if i == length - 1:
                    res.append(target.val)
                if target.left:
                    q.append(target.left)
                if target.right:
                    q.append(target.right)

        return res

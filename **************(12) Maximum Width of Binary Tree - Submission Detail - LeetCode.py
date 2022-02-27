 #Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        qs = [(root, 0)]
        width = 0
        
        while len(qs) > 0:
            width = max(width, qs[-1][1] - qs[0][1] + 1)
            next_qs = []
            for q, p in qs:
                if q.left:
                    next_qs.append((q.left, p * 2))
                if q.right:
                    next_qs.append((q.right, p * 2 + 1))
            qs = next_qs
        
        return width

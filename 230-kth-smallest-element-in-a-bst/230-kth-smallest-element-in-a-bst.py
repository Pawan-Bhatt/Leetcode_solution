# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        pos = 0
        ans = 0
        
        current = root
        
        while current and pos < k:
            
            if not current.left:
                pos += 1
                ans = current.val
                current = current.right
            
            else:
                pre = current.left
                while pre.right:
                    pre = pre.right
                
                pre.right = current
                left = current.left
                current.left = None
                current = left
        
        return ans

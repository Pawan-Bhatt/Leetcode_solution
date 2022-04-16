# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, init):
            if not node: return 0
            
            r_sum = dfs(node.right, init)
            orig, node.val = node.val, node.val + init + r_sum
            l_sum = dfs(node.left, node.val)
            
            return r_sum + orig + l_sum
                       
        dfs(root, 0)
        return root
        
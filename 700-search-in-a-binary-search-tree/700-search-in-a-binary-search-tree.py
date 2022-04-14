# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val: # If end is reached or a node with a value of target is found found.
            return root # Return that node.
		# If target > current nodes value search in left side of node else search rightwards.
        return self.searchBST(root.left,val) if root.val > val else self.searchBST(root.right,val) 
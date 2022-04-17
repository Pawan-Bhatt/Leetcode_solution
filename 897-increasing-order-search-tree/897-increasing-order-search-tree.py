# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(rt: Optional[TreeNode], node: TreeNode) -> TreeNode:
            if rt is not None:
                node = inorder(rt.left, node)

                node.right = TreeNode(val=rt.val)
                node = node.right

                node = inorder(rt.right, node)

            return node

        dummy_node = TreeNode()
        inorder(root, dummy_node)

        return dummy_node.right
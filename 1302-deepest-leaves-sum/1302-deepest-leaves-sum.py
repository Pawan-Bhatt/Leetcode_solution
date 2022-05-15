# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue: # iterates through the layers
            lastSum, newQueue = 0, list() # init sum to zero
            while queue: # current layer's nodes
                node = queue.pop(0)
                lastSum += node.val # sum of the last layer is accumulated here
                if any([node.left, node.right]): # build next layer
                    if node.left: newQueue.append(node.left)
                    if node.right: newQueue.append(node.right)
            queue = newQueue # next layer
        return lastSum
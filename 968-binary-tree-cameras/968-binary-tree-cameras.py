# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        MONITOR_HASCAMERA=0
        MONITOR_NOCAMERA=1
        NOT_MONITORED=2
        def checkCam(root,par)->int:
            nonlocal ans
            if root==None:
                return MONITOR_NOCAMERA
            left=checkCam(root.left,root)
            right=checkCam(root.right,root)
            if left==MONITOR_NOCAMERA and right==MONITOR_NOCAMERA:
                return NOT_MONITORED
            elif left==NOT_MONITORED or right==NOT_MONITORED:
                ans+=1
                return MONITOR_HASCAMERA
            else:
                return MONITOR_NOCAMERA
        ans=0
        val=checkCam(root,None)
        if val==NOT_MONITORED:
            ans+=1
        return ans
        
            
        
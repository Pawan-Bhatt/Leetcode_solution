# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        prev1 = prev1_head = ListNode(-1)
        prev2 = prev2_head = ListNode(-1)
        
        while head:
            if head.val < x:
                prev1.next = head
                prev1 = prev1.next
            else:
                prev2.next = head
                prev2  = prev2.next 
            head = head.next 
        
        prev2.next = None
        prev1.next  = prev2_head.next
        return prev1_head.next
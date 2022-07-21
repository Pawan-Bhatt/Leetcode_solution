# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p_prev, p = None, head
        for _ in range(left - 1):
            p_prev, p = p, p.next
        
        prev, cur = p, p.next
        for _ in range(right - left):
            cur.next, prev, cur = prev, cur, cur.next

        p.next = cur
        if p_prev:
            p_prev.next, prev = prev, head
        
        return prev
            
        
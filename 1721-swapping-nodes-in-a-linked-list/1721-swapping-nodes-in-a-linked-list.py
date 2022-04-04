# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # start and end pointer:
        fast, slow = dummy, dummy
         
        for i in range(k):
            prev_fast = fast # the node right before the fast (k-1)th node
            fast = fast.next # fast is at the kth node after iteration
            
        kth_node = fast
        
        while fast.next:
            slow = slow.next # slow is at the (k+1)th node from the last
            fast = fast.next
            
        end_kth_node = slow.next
        temp = kth_node.val
        kth_node.val = end_kth_node.val
        end_kth_node.val = temp
        
#         end_kth_node = slow.next # the kth node from the last
#         slow.next = kth_node
#         prev_fast.next = end_kth_node
        

#         kth_next = kth_node.next                
#         kth_node.next = end_kth_node.next
#         end_kth_node.next = kth_next

        return dummy.next
        
        
        
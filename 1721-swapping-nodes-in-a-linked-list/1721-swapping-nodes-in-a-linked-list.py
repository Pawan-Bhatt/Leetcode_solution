# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr[k-1] , arr[-k] = arr[-k] , arr[k-1]
        new_lst = curr = ListNode(0)
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return new_lst.next
        
            
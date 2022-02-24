# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values=[]
        temp=head
        while temp!=None:
            values.append(temp.val)
            temp=temp.next
            
        values.sort()
        i=0
        temp=head
        while i<len(values):
            temp.val=values[i]
            i+=1
            temp=temp.next
            
        return head
            
        

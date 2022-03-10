class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = sm = ListNode()                            # head: we get the start to return, sm: to iterate and link the new sum nodes.
        carry = 0                                         # carry starts with zero
        while l1 or l2:                                   # we are using or, because list sizes might not be equal.
            if l1: carry, l1 = carry + l1.val, l1.next    # if l1 is not null, add it to carry and update l1 to its next.
            if l2: carry, l2 = carry + l2.val, l2.next    # if l2 is not null, add it to carry and update l2 to its next.
            sm.next = sm = ListNode(val = carry % 10)     # make a new node with carry % 10(because carry can be greater than 9, ie two digits) and link the sm.next to it and now this new node is our sm
            carry //= 10                                  # if carry is greater than 9, means we have to add it in next iteration
        if carry: sm.next = ListNode(val = carry)         # what if there is non zero carry left to be added.
        return head.next                                  # return head.next bcoz head is pointing to dummy node.

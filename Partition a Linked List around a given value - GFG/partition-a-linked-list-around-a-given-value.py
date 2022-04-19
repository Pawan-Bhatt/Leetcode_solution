#User function Template for python3

"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def insert_to_list(self, node, list_tail):
        node.next = None
        list_tail.next = node
        return node
        
    def partition(self, head, x):
        #code here
        less_head = less_itr = Node(None)
        equal_head = equal_itr = Node(None)
        greater_head = greater_itr = Node(None)
        itr = head
        while itr:
            future = itr.next
            if itr.data < x:
                less_itr = self.insert_to_list(itr, less_itr)
            elif itr.data == x:
                equal_itr = self.insert_to_list(itr, equal_itr)
            else:
                greater_itr = self.insert_to_list(itr, greater_itr)
            itr = future
            
        less_head = less_head.next
        equal_head = equal_head.next
        greater_head = greater_head.next
        
        if equal_head:
            equal_itr.next = greater_head
        if less_head:
            less_itr.next = equal_head or greater_head
        head = less_head or equal_head or greater_head
        return head

        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.partition(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends
#User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to merge two sorted linked list.


def sortedMerge(head1, head2):
   # code here
   current1=head1
   current2=head2
   while current1.next!=None:
       current1=current1.next
   current1.next=head2
   stack=[]
   current=head1
   while current!=None:
       stack.append(current.data)
       current=current.next
   stack.sort(reverse=True)
   current3=head1
   while current3!=None:
       current3.data=stack.pop()
       current3=current3.next
   return head1
            
    # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        
        printList(sortedMerge(a.head,b.head))

# } Driver Code Ends
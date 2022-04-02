#User function Template for python3

# Linked List Node Structure

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None  '''
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
  
    def push(self, val):
  
    # 1 & 2: Allocate the Node & 
    #        Put in the data 
        new_node = Node(val) 
          
    # 3. Make next of new Node as head 
        new_node.next = self.head 
          
    # 4. Move the head to point to new Node  
        self.head = new_node 
    
    def moveZeroes(self):
        temp = self.head
        curr = self.head.next
        while(curr is not None):
            if curr.data == 0:
                temp.next = curr.next
                curr.next = self.head
                self.head = curr
                curr = temp.next
                continue
            temp = temp.next
            curr = curr.next
        #code here
    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        lis = LinkedList()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        #head = createList(arr, n)
        for i in range(0,len(arr)):
            lis.push(arr[i])
        lis.moveZeroes()
        lis.display()
        print()
# } Driver Code Ends

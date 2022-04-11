#User function Template for python3
import numpy as np 
class Solution:
    def merge(self, arr1, arr2, n, m):
        # code here
       i = 0 
       while i < m :
           arr1.append(arr2[i])
           i += 1
           
       arr1.sort() 
       arr2.clear() 
       
       j = 0
       while j < m :
           arr2.append(arr1[n+m-j-1])
           arr1.pop() 
           j += 1
       
       arr2.sort()
           
       return 
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, m=map(int, (input().strip().split()))
        arr1=list(map(int , input().strip().split()))
        arr2=list(map(int , input().strip().split()))
        ob = Solution()
        ans=ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends
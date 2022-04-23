#User function Template for python3


#Binary  Search does it

class Solution:
   def binarySearch(self,a,value):
       left=0
       right=len(a)-1
       while True:
           mid=(left + right)//2
           if value==a[mid]:
               return mid
           if value<a[mid]:
               right=mid-1
           else:
               left=mid+1
           if left>right:
               return left
       
   def searchInsertK(self, arr, n, k):
       # code here
           result=self.binarySearch(arr,k)
           return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends
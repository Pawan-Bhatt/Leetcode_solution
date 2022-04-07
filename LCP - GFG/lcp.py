#User function Template for python3

class Solution:
    def LCP(self,arr,n):
        if n==0: return ""
        if n==1: return arr[0]
        arr.sort()
        end=min(len(arr[0]),len(arr[n-1]))
        i=0
        while i<end and arr[0][i]==arr[n-1][i]: i+=1
        prefix=arr[0][0:i]
        if len(prefix)==0: return "-1"
  
        return prefix
            
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs =int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[ x  for x in input().split()]
        obj=Solution()
        print(obj.LCP(arr,n))
# } Driver Code Ends
#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        summ = 0
        newsumm = 0
        for i in range(1 ,n+1):
            summ += i
        for i in array:
            newsumm += i
        return summ-newsumm
        
            
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends
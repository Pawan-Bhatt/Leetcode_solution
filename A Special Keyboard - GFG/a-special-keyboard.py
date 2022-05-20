#User function Template for python3

class Solution:
    def findTime(self, S1, S2):
        ans = 0
        k = list(S2)
        prev=0
        for i in S2:
            ans+=abs(S1.index(i)-prev)
            prev=S1.index(i)
        return ans
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S1=input()
        S2=input()
        
        ob = Solution()
        print(ob.findTime(S1,S2))
# } Driver Code Ends
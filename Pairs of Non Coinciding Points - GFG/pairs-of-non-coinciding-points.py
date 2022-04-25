#User function Template for python3
from collections import defaultdict
class Solution:
    def numOfPairs(self, X, Y, N):
        xc = defaultdict(int)
        yc = defaultdict(int)
        xyc = defaultdict(int)
        
        ans = 0
        for x, y in zip(X, Y):
            ans += xc[x] + yc[y] - xyc[(x, y)]*2
            xc[x] += 1
            yc[y] += 1
            xyc[(x, y)] += 1
            
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        X=list(map(int,input().split()))
        Y=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.numOfPairs(X,Y,N))
# } Driver Code Ends
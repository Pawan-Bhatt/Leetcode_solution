
class Solution:
    def karyTree(self, k, m):
        return pow(k,m,1000000007)
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        k,m=map(int,input().split())
        
        ob = Solution()
        print(ob.karyTree(k,m))
# } Driver Code Ends
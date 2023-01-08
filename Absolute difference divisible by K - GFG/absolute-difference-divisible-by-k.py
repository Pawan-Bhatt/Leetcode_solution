#User function Template for python3

class Solution:
    def countPairs (self, n, arr, k):
        # code here
        ans=0
        mp=dict()
        for ele in arr:
            if ele%k in mp:
                ans+=mp[ele%k]
                mp[ele%k]+=1
            else:
                mp[ele%k]=1

        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        k=int(input())
        
        ob = Solution()
        print(ob.countPairs(n,arr,k))
# } Driver Code Ends
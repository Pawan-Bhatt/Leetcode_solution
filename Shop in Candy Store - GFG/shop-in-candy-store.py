#User function Template for python3

class Solution:

    def candyStore(self, candies,N,K):
        candies.sort()
        low = high = 0
        get = N
        for i in range(N):
            low = low+candies[i]
            high = high+candies[get-i-1]
            N-=(1+K)
            if(N<=0):
                break
        return [low,high]
            
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        N,K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies,N,K))
# } Driver Code Ends
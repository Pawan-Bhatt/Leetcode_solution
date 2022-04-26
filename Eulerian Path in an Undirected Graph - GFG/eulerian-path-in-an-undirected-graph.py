# User function Template for Python3

class Solution:
    def eulerPath(self, N, graph):
        ans=0
        for i in graph:
            if sum(i)%2==0:
                ans+=1
            if ans==N-2:
                return 1
        return 0

#{ 
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        graph = []
        for i in range(N):
            graph.append(list(map(int, input().strip().split())))
        
        ob = Solution()
        print(ob.eulerPath(N, graph))
# } Driver Code Ends
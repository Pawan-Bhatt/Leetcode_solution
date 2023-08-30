class Solution:
    def snakeCase(self, S , n):
        ans = ''
        return (S.replace(' ', '_')).lower()
        # S = S.replace(' ', '_')
        # for i in S:
        #     if i==" ":
        #         ans+="_"
        #     else:
        #         ans+=i
        # return S.lower()
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        S=input()
        
        ob = Solution()
        print(ob.snakeCase(S , n))
# } Driver Code Ends
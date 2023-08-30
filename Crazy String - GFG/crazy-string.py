#User function Template for python3

class Solution:

    def getCrazy(self, s):
        ans = ''
        k = s[0].isupper()
        if k == True:
            for i in range(len(s)):
                if i%2==0:
                    ans+=s[i].upper()
                else:
                    ans+=s[i].lower()
        else:
            for i in range(len(s)):
                if i%2!=0:
                    ans+=s[i].upper()
                else:
                    ans+=s[i].lower()
            
        # code here
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.getCrazy(S))
# } Driver Code Ends
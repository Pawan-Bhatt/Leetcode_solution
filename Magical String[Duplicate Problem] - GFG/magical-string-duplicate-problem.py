#User function Template for python3
class Solution:
    def magicalString (ob,S):
        ans = ''
        S.lower()
        for i in S:
            k = ord(i)
            num = k-97
            ans+= chr(122-num)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.magicalString(S))
# } Driver Code Ends
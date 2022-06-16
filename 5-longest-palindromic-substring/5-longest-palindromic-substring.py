class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand_pallindrome(i,j):            
            while 0<=i<=j<n and s[i]==s[j]:
                i-=1
                j+=1                            
            return (i+1, j)
        
        res=(0,0)
        for i in range(n):
            b1 = expand_pallindrome(i,i)
            b2 = expand_pallindrome(i,i+1)            
            res=max(res, b1, b2,key=lambda x: x[1]-x[0]+1) # find max based on the length of the pallindrome strings.
                    
        return s[res[0]:res[1]]    
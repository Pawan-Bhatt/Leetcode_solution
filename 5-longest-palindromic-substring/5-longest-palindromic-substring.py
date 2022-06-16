class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 1 or s == s[::-1]:
            return s
        
        start, maxlen= 0, 1
        for i in range(1, len(s)):
            
            odd = s[i - maxlen - 1:i + 1]
            even = s[i - maxlen:i + 1]
            if i - maxlen - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlen - 1
                maxlen += 2
                
            if i - maxlen >= 0 and even == even[::-1]:
                start = i - maxlen
                maxlen += 1
        return s[start:start + maxlen]
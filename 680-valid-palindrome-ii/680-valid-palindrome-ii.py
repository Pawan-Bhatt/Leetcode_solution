class Solution:
    def validPalindrome(self, s: str) -> bool:
        
#         # Approach 1: Backtrack
#         # O(n^2) time O(n) space
        
#         def isPalindrome(word):
#             l, r = 0, len(word)-1
#             while l <= r:
#                 if word[l] != word[r]:
#                     return False
#                 l+=1
#                 r-=1
                
#             return True
        
#         def backtrack(idx, currWord):
#             if idx == len(s)+1:
#                 return False
#             if isPalindrome(currWord):
#                 return True
            
#             return backtrack(idx+1, s[:idx] + s[idx+1:])
        
#         return backtrack(0, s)
    
#         # Approach 2: Iteration
#         # O(n^2) time O(1) space
        
#         for i in range(len(s)):
#             if isPalindrome(s[:i]+s[i+1:]):
#                 return True
            
#         return False
    
        # Approach 3:
        
        if s == s[::-1]:
            return True
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                removeL = s[:l] + s[l+1:]
                removeR = s[:r] + s[r+1:]
                return removeL == removeL[::-1] or removeR == removeR[::-1]
                
       
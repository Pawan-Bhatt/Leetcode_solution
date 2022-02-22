class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        k = ord('Z')-ord('A') # 
        # 1 * 26 +2
        ans = 0
        for item in columnTitle:
            ans = ans  * 26 + ord(item) - ord("A") +1
        return ans
    

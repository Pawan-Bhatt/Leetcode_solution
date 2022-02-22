class Solution:
    def reverse(self, x: int) -> int: 
        ans = 0
        mod = 0 
        is_neg = False 
        if x<0:
            x = x * (-1)
            is_neg = True
        while (x)!=0:
            mod = x % 10
            ans = ans*10 + mod
            x = x//10
        if is_neg == True:
            ans = ans*(-1)
        if ans > 2**31 -1:
            return 0
        if ans < -2**31:
            return 0
        return ans
        
        

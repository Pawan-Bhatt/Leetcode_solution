class Solution:
    def minimumTotal(self, a: List[List[int]]) -> int:
        n=len(a)
        dp=[[0] * (n+1) for _ in range(n+1)]
        for level in range(n-1,-1,-1):
            for i in range(level+1):
                dp[level][i]=a[level][i] + min(dp[level+1][i], dp[level+1][i+1])
        return dp[0][0] 
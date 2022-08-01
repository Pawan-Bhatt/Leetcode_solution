class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[1] * n ] * m
        for i in range(1,m):
            for j in range(1,n):
                ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[m-1][n-1]
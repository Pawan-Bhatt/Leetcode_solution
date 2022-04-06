class Solution:
    max_val = 10 ** 9 + 7
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        res = 0
        n = len(arr)
        
        # i: obj, j: weight, k: choice -> cnt
        dp = [[[0] * 3 for _ in range(target + 1)] for _ in range(n)]
        dp[0][arr[0]][0] = 1
        
        for i in range(1, n):
            for j in range(target + 1):
                dp[i][j][0] = dp[i-1][j][0]
                if j == arr[i]:
                    dp[i][j][0] += 1
                    
                for k in range(1, 3):
                    if j - arr[i] >= 0:
                        dp[i][j][k] = (dp[i-1][j][k] + dp[i-1][j-arr[i]][k-1]) % self.max_val
                    else:
                        dp[i][j][k] = dp[i-1][j][k]

        return dp[n-1][target][2]
        
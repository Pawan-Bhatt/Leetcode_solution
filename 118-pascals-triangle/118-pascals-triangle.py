class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		dp = [[1]]

		for r in range(numRows-1):
			newDp = [1]
			for c in range(1, r+1):
				newDp.append(dp[r][c-1]+dp[r][c])
			newDp.append(1)
			dp.append(newDp)

		return dp
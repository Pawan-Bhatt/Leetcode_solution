import bisect
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        for s in word2:
            for i in reversed(range(len(word1))):
                v = word1[i]
                if v == s:
                    ind = bisect.bisect_left(dp, i)
                    if ind == len(dp):
                        dp.append(i)
                    else:
                        dp[ind] = i
        return len(word1) + len(word2) - len(dp) * 2   
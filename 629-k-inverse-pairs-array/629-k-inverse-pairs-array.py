class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0 : return 1
        count = [1] + [0 for x in range(k)]
        for j in range(1, n):
            new_count = [1] + [0 for x in range(k)]
            tmp = 1
            for i in range(1, k+1):
                tmp += count[i]
                if i >= j+1:
                    tmp -= count[i-j-1] 
                new_count[i] = tmp
            count = new_count
        return count[-1] % (10**9+7)
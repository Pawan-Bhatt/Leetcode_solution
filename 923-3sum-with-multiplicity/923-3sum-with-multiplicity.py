class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 1_000_000_007
        seen = Counter(A)
        A = list(set(A))
        A.sort()
        n = len(A)
        ans = 0
        for i in range(n):
            need = target - A[i]
            obs = set()
            for x in A[i:]:
                obs.add(need - x)
                if x > need:
                    break
                if x in obs:
                    a, b, c = sorted([A[i], x, need - x])
                    if a < b < c:
                        ans += seen[a] * seen[b] * seen[c]
                    if a == b < c:
                        ans += seen[a] * (seen[a] - 1) * seen[c] // 2
                    if a < b == c:
                        ans += seen[a] * seen[b] * (seen[b] - 1) // 2
                    if a == b == c:
                        ans += seen[a] * (seen[a] - 1) * (seen[a] - 2) // 6
                    ans %= MOD
                    
        return ans
        
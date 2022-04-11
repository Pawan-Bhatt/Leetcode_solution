class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        k %= (m * n)
        
        flat = tuple(grid[i][j] for i in range(m) for j in range(n))
        
        flat = flat[-k:] + flat[:-k]
        
        ans = [[flat[i * n + j] for j in range(n)] for i in range(m)]
        
        return ans
#         l, m, n, k = [num for row in grid for num in row], len(grid), len(grid[0]), k % (len(grid) * len(grid[0]))  # grid to list
#         l = l[-k:] + l[:-k]  # shift k times
#         return [l[i * n: i * n + n] for i in range(m)]  # list to grid
        
        
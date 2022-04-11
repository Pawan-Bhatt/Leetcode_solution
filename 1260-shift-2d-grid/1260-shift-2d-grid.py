class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l, m, n, k = [num for row in grid for num in row], len(grid), len(grid[0]), k % (len(grid) * len(grid[0]))  # grid to list
        l = l[-k:] + l[:-k]  # shift k times
        return [l[i * n: i * n + n] for i in range(m)]  # list to grid
        
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def helper(value):
            stack = [(0, 0)]
            seen = {(0, 0)}
            
            while stack:
                (x, y) = stack.pop()
                if x == m - 1 and y == n - 1:
                    return True
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    if 0 <= p < m and 0 <= q < n: 
                        if (p, q) not in seen: 
                            effort = abs(heights[p][q] - heights[x][y])
                            if effort <= value: 
                                seen.add((p, q))
                                stack.append((p, q))
                                
            return False 
        
        m, n = len(heights), len(heights[0])
        
        start = -1
        end = max(max(row) for row in heights)
        
        while end - start > 1: 
            mid = (end + start)//2
            if helper(mid):
                end = mid
            else: 
                start = mid
                
        return end 
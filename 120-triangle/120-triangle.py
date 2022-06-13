class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for idx_row in range(1, len(triangle)):
            triangle[idx_row][0] += triangle[idx_row-1][0]
            triangle[idx_row][-1] += triangle[idx_row-1][-1]
            for i in range(1, len(triangle[idx_row-1])):
                triangle[idx_row][i] += min(triangle[idx_row-1][i-1], triangle[idx_row-1][i])
        
        return min(triangle[-1])
                
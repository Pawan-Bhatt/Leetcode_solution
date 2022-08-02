class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        new = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new.append(matrix[i][j])
        new.sort()
        return new[k-1]
        
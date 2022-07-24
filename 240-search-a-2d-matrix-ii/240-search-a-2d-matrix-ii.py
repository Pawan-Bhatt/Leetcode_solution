class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ele in matrix:
            for new in ele:
                if target == new:
                    return True
                new+=1
        return False
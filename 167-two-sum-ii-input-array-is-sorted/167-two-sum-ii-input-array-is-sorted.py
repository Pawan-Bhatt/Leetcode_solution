class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        needed = {}
        
        for index, num in enumerate(numbers):
            if num not in needed:
                needed[target-num] = index
            else:
                return [needed[num]+1, index+1]
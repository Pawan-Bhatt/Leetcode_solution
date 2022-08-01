class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i , j in enumerate(nums):
            r = target - j
            if r in dic:
                return [dic[r] , i]
            dic[j] = i
        return []
        
        
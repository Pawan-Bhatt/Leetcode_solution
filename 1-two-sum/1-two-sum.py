class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if nums[i] + nums[j] == target:
                    return [i , j]
                j+=1
                    
        return []
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dic = {}
#         for i , j in enumerate(nums):
#             r = target - j
#             if r in dic:
#                 return [dic[r] , i]
#             dic[j] = i
#         return []
            
        
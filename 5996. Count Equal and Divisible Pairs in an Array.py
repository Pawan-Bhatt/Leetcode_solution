class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        i=0
        while i< len(nums)-1:
            j = i+1
            while j<len(nums):
                if nums[i] == nums[j]:
                    if (i*j) %k == 0:
                        count +=1
                j+=1
            i+=1
        return count
                
        

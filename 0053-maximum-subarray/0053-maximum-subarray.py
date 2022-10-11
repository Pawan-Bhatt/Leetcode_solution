class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        max_sum =  -10000
        for i in range(len(nums)):
            curr_max = curr_max + nums[i]
            if (curr_max >max_sum ):
                max_sum = curr_max
            if (curr_max < 0):
                curr_max = 0
        return max_sum
        
        
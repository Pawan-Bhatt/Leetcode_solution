class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res=[nums[0]]
        i=1
        while i<len(nums) and nums[i]==nums[i-1]:
            i+=1
        if i<len(nums):
            res.append(nums[i])
        
        while i<len(nums):
            if (res[-1] > res[-2]):  # last sequence was incresing
                while i<len(nums) and nums[i]>=nums[i-1]:
                    res[-1] = nums[i]
                    i+=1
                if i<len(nums):
                    res.append(nums[i])
                    i+=1
            else:
                while i<len(nums) and nums[i]<=nums[i-1]:
                    res[-1]=nums[i]
                    i+=1
                if i<len(nums):
                    res.append(nums[i])
                    i+=1
        return len(res)
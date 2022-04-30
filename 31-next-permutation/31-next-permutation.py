class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    p = len(nums) - 2
    
    while p != -1 :
      if nums[p] >= nums[p+1] : p -= 1
      else :
        print(nums[p])
        nums[p]
        l = len(nums) - 1
        while nums[p] >= nums[l] : l -= 1
        nums[p], nums[l] = nums[l], nums[p]
        p += 1
        l = len(nums) - 1
        while p < l :
          nums[p], nums[l] = nums[l], nums[p]
          p += 1
          l -= 1
        return nums
        
    nums.reverse()    
    return nums
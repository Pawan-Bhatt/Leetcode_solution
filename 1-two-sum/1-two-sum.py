class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                previousIndex = dic[target-nums[i]]
                return [previousIndex, i]
            dic[nums[i]] = i
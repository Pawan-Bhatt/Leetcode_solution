class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cur_diff, cnt = -1, 0
        res = 0
        for i in range(1, len(nums)):
            new_diff = nums[i] - nums[i-1]
            if new_diff != cur_diff:
                cur_diff, cnt = new_diff, 1
            else:
                res += cnt
                cnt += 1
        return res

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        k = None
        prev = curr = 0
        
        for num in sorted(count):
            earn = num * count[num]
            
            if num - 1 == k:
                prev, curr = curr, max(prev + earn, curr)
            else:
                prev, curr = curr, curr + earn
                
            k = num
        
        return curr
        

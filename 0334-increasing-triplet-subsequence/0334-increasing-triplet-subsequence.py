class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = inf 
        j = inf 
        for k in nums:
            if k > j:
                return True
            if k <=i:
                i =k
            else :
                j = k
        return False
        
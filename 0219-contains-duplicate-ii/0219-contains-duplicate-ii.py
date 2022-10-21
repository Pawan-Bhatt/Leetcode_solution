class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create dictionary for Lookup
        lookup = {}
        
        for i in range(len(nums)):
            
            # If num is present in lookup and satisfy the condition return True
            if nums[i] in lookup and abs(lookup[nums[i]]-i) <= k:
                return True
            
            # If num is not present in lookup then add it to lookup
            lookup[nums[i]] = i
        
        return False
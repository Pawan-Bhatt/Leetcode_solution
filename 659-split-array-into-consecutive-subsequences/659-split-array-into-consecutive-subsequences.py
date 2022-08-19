class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        seq = defaultdict(int)      # key: ending number, val: how many seqs
        left = Counter(nums)        # key: number, val: how many of key are left unchecked
        
        for num in nums:
            if (not left[num]): continue   # the number is already in seqs, we don't need to check again
            
            if (seq[num-1] > 0):    # If there is sequence before the number, we add the number to the seq
                seq[num-1] -= 1 
                seq[num] += 1
                left[num] -= 1
                
            else:   # If not we create a new seq using the number
                if (not left[num+1] or not left[num+2]):  #  If there aren't two numbers behind to let us create new seq, return False
                    return False
                left[num] -= 1
                left[num+1] -= 1
                left[num+2] -= 1
                seq[num+2] += 1
        
        return True
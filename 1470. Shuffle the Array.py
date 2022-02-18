class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num = n*2
        mid = n
        mm  = []
        kk = []
        rr = []
        for i in range(n):
            kk.append(nums[i])
        for i in range(n , num):
            mm.append(nums[i])
        for i in range(n):
            rr.append(kk[i])
            rr.append(mm[i])
        return rr
            
    

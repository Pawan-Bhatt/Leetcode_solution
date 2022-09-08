class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new = []
        for i in range(1,len(nums),2):
            fre = nums[i-1]
            while(fre>0):
                new.append(nums[i])
                fre-=1
        return  new
        
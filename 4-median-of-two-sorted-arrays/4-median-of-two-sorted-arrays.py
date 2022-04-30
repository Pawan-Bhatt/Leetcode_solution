class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        index = (length-1)//2
        
        if length%2 == 0:
            final_ans = (nums1[index]+nums1[index+1])/2
            
        else:
            final_ans = nums1[index]
            
        return final_ans
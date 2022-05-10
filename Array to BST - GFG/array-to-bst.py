# class Solution:
# 	def sortedArrayToBST(self, nums):
# 	    s = 0
# 	    l = len(nums)-1
# 	    root = self.newtree(nums , s , l , [])
# 	    return root
	        
# 	    # code here
# 	    def newtree(self , nums , s , l , ans):
# 	        if(s>l):
# 	            return
# 	        mid = (s+l)//2
# 	        root = (nums[mid])
# 	        ans.append(root)
# 	        self.newtree(nums , s , mid-1 , ans)
# 	        self.newtree(nums , mid+1 , l , ans)
# 	        return ans
class Solution:
    def sortedArrayToBST(self, nums):
        s=0
        e=len(nums)-1
        root=self.makingtree(nums,s,e,[])
        return root
    def makingtree(self,nums,s,e,ans):
        if(s>e):
            return 
        mid=(s+e)//2
        root=(nums[mid])
        ans.append(root)
        self.makingtree(nums,s,mid-1,ans)
        self.makingtree(nums,mid+1,e,ans)
        return ans
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.sortedArrayToBST(nums)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends
class Solution:
	def isRepeat(self, s):
		# code here
		for i in range(1,len(s)//2+1):
		    if(len(s)%i!=0):
		        continue
		    if(s[:i]*(len(s)//i) == s):
		        return 1 
		return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.isRepeat(s)
		
		print(answer)


# } Driver Code Ends
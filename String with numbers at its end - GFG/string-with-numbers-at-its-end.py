#User function Template for python3
class Solution:
	def isSame(self, s):
	    count = 0
	    k = ''
	    for i in range(len(s)):
	        if ord(s[i])>=97 and ord(s[i])<=122:
	            count+=1
	        else:
	            k +=s[i]
	    if int(k)==count:
	        return 1
	    return 0
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.isSame(s)
		
		print(answer)


# } Driver Code Ends
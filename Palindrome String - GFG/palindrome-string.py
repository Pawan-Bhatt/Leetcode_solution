#User function Template for python3
class Solution:
	def isPalindrome(self, S):
	    i = 0
	    j = len(S)-1
	    k = (len(S)//2)
	    if j<2:
	        if j<1:
	            return 1
	        elif S[0]==S[1]:
	            return 1
	        else:
	            return 0
	    else:
    	    while i<k:
    	        if S[i]!=S[j]:
    	            return 0
    	            break
    	        i+=1
    	        j-=1
    	    return 1
	    
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lastIndex(self, s):
        k = len(s)
        if len(s)==1 and s[0]=='1':
            return 0
        for i in range(k-1,-1,-1):
            if s[i]=='1':
                return i
                break
        return -1
        # code here
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	s = input()
    	ob = Solution()
    	print(ob.lastIndex(s))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
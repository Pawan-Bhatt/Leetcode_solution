#User function Template for python3
class Solution:
    def findSubString(self, str):
        ans_len = len(set(str))
        d = {}
        ws = 0
        ans = 10**6 
        for we in range(0,len(str)):
            d[str[we]] = d.get(str[we],0)+1
            if len(d)==ans_len:
                while d[str[ws]] >1:
                    d[str[ws]] -= 1
                    ws += 1
                ans = min(ans,we-ws+1)
        return ans
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	str = input()
    	ob=Solution()
    	print(ob.findSubString(str))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countShare(self,B):
        count = 0 
        l = B
        max_sq = int((l - 2)/2)
        while max_sq > 0:
            count += max_sq
            max_sq = max_sq - 1
        return count
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        b=int(input().strip())
        obj=Solution()
        print(obj.countShare(b))
        
# } Driver Code Ends
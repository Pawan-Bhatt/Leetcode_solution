#User function Template for python3
from collections import Counter
class Solution:
    def firstNonRepeating(self, arr, n): 
        c=Counter(arr)
        for i in arr:
            if c[i]==1:
                return i
        return 0
        # Complete the function


#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends
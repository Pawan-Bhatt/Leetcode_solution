#User function Template for python3

class Solution:
    def check(self,p,n):
        temp = p
        count = 0
        f = 5
        while (f <= temp):
            count += temp//f
            f = f*5
     
        return (count >= n)
    def findNum(self, n : int):
        if (n==1):
            return 5
  
        # Initializing low and high for binary
        # search.
        low = 0
        high = 5*n
  
        # Binary Search.
        while (low <high):
 
            mid = (low + high) >> 1
  
            # Checking if mid's factorial contains
            # n trailing zeroes.
            if (self.check(mid, n)):
                high = mid
            else:
                low = mid+1
         
      
        return low
        # Complete this function

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends
#User function Template for python3

class Solution:
   def largestNum(self,n,s):
       if(s > (n*9)):
           return -1
       Res = 0
       for i in range(n):
           if(s >= 9):
               Res *= 10
               Res += 9
               s -= 9
           else:
               Res *= 10
               Res += s
               s -= s
       return Res
                
        
        
        # code here
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends
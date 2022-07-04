#User function Template for python3
class Solution:
    def minVal(self, a, b):
       cb = 0
       for i in range(32):
           if((1<<i)&b):
               cb += 1
       if(cb==0):
           return 0
       x = 0
       for i in range(31,-1,-1):
           if((1<<i)&a):
               x ^= (1<<i)
               cb -= 1
               if(cb==0):
                   return x
       for i in range(32):
           if(x&(1<<i)==0):
               x ^= (1<<i)
               cb -= 1
               if(cb==0):
                   return x

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        b = int(input())
        
        ob= Solution()
        print(ob.minVal(a,b))
# } Driver Code Ends
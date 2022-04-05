#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       start = 0
       index = 0
       sum = 0
       while index < n and start < n:
           if arr[index] == s:
               return [index+1,index+1]
           if sum < s:
               sum += arr[index]
               index += 1
           if sum > s:
               sum -= arr[start]
               start += 1
           if sum == s:
               return [start+1,index]
           
       return [-1]
        
       #Write your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
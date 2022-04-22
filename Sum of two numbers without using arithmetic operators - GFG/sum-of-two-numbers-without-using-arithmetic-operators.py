#User function Template for python3

def sum(a,b):
    if not b :
        return a
    if not a :
        return b
    carry = a&b
    a = a^b
    b = carry<<1
    return sum(a,b)
    #code here

#{ 
#  Driver Code Starts
import math
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        inp = list(map(int,input().split())) 
        
        a=inp[0]
        b=inp[1]
        
        #ob=Solution()
        print(sum(a,b))
     
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
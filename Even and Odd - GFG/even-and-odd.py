#User function Template for python3

class Solution:
    def reArrange(self, arr, N):
        # code here 
        i=0
        j=1
        k=0
        while(k<N and i<N and j<N):
            if(arr[k]%2==0):
                t=arr[k]
                arr[k]=arr[i]
                arr[i]=t
                i+=2
                if(i<j):
                    k=i
                else:
                    k=i
                    
            else:
                t=arr[k]
                arr[k]=arr[j]
                arr[j]=t
                j+=2
                if(i<j):
                    k=i
                else:
                    k=j
        return arr
            
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def check(arr, n):
    flag = 1
    c=d=0
    for i in range(n):
        if i%2==0:
            if arr[i]%2:
                flag = 0
                break
            else:
                c+=1
        else:
            if arr[i]%2==0:
                flag = 0
                break
            else:
                d+=1
    if c!=d:
        flag = 0
            
    return flag
        
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ob.reArrange(arr,N)
        
        print(check(arr,N))

# } Driver Code Ends
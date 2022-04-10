#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        zero = 0
        one = 0
        two = 0
        for i in range(n):
            if arr[i] == 0:
                zero+=1
            elif arr[i] == 1:
                one+=1
            elif arr[i] == 2:
                two+=1
        i = 0
        while zero!=0:
            arr[i] = 0
            i+=1
            zero-=1
        while one!=0:
            arr[i] = 1
            i+=1
            one-=1
        while two!=0:
            arr[i] = 2
            i+=1
            two-=1
        return arr
        # code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
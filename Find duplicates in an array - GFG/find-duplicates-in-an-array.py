class Solution:
    def duplicates(self, arr, n):
        result = []
        for i in range(n):
               arr[arr[i] % n] += n
    
        for i in range(n):
            if arr[i]//n > 1:
                result.append(i)
            
        if not result:
            return [-1]
        else:
            return result
            
    	# code here
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
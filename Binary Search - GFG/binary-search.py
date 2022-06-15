#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		
        def search(arr, startIndex, endIndex, k):

            mid_length = (endIndex - startIndex) // 2
            mid_index = (endIndex + startIndex) // 2
    
            if arr[mid_index] == k:
                return mid_index
    
            if mid_length == 0:
                return -1
    
            if arr[mid_index] < k:
                return search(arr, startIndex + mid_length, endIndex, k)
            else:
                return search(arr, startIndex, startIndex + mid_length, k)
    
        return search(arr, 0, n, k)
		# code here

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends
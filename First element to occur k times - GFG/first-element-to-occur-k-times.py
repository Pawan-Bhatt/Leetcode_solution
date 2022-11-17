#User function Template for python3


class Solution:
    def firstElementKTime(self,  a, n, k):
        dictionary = {}
        
        if (k == 1):
            return a[0]
        for index, value in enumerate(a):
            if value not in dictionary:
                dictionary[value] = 1
 
            else:
                dictionary[value] += 1
                if dictionary[value] == k:
                    return value
                    
        return -1
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
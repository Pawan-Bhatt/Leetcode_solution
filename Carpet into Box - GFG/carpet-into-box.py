#User function Template for python3


class Solution:
    def carpetBox(self, A,B,C,D):
        #code here
        if A>B:
            A,B = B,A
        if C>D:
            C,D = D,C
        c = 0
        while A>C or B>D:
            if A>C and B>D:
                B = B // 2
            elif A>C:
                A = A // 2
            else:
                B = B // 2
            if A > B:
                A,B = B,A
            c += 1
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            A,B,C,D = map(int, input().split())
            
            obj = Solution()
            print(obj.carpetBox(A,B,C,D))
            
            T-=1


if __name__ == "__main__":
    main()


# } Driver Code Ends
#User function Template for python3

def getMinMax( a, n):
    max_num = 0
    min_num = 10**12
    for i in range(n):
        if a[i] < min_num :
            min_num = a[i]
        if a[i] > max_num :
            max_num = a[i]
    return min_num , max_num
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends
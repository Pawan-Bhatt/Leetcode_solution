#User function Template for python3

def reverseWord(s):
    ans = ''
    i = len(s)-1
    while i>=0:
        ans+=s[i]
        i-=1
    return ans
    #your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends
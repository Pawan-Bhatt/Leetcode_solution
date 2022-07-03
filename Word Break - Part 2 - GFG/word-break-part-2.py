#User function Template for python3
class Solution:
    lst = []
    
    def wordBreak(self, n, words, s):
        self.lst = []
        self.solve(words, s, "")
        return self.lst
        
    def solve(self, words, s, result_string):
        for word in words:
            # init
            result_str = result_string
            
            # final word
            if s == word:
                result_str = result_str + " " + word
                self.lst.append(result_str.strip())
            
            # search next word and continue
            if s.startswith(word):
                result_str = result_str + " " + word
                self.solve(words, s[len(word):], result_str)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dict = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dict, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends
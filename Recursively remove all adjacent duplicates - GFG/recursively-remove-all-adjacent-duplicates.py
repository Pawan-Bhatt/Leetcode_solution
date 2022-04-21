"""
Do not search for equal characters, search for unequal characters
Add values to a new string as and when neighboring elements do not match
"""
class Solution:
   def remove (self, s):
       #code here
       news=""#New String
       #print(s)
       n=len(s)#Length of originl string
       
       while True:
           news=""
           
           oldn=n#Keep the length for comparison at the end
           
           s= s + "1"#Add a sentinel at the end
           p1=0
           
           for i in range(1,n+1):
               if s[i]!=s[i-1]:#New element found
                   p2=i
                   if p2-p1<=1:#Previous matched sequence was of 1 element only. Add it
                       news=news + s[i-1]
                   p1=p2
           n=len(news)#New length
           if n==oldn:#No changes happened. Answer found.Return
                return news
           s=news#Repeat with new string
       #return news

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.remove(S))


# } Driver Code Ends
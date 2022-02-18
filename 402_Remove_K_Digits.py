class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for c in num:
            while len(stack)!=0 and k>0 and stack[len(stack)-1]>c:
                stack.pop()
                k-=1
            stack.append(c)
        while k>0 and len(stack)!=0:
            stack.pop()
            k-=1
        s=""
        nonZero=False
        for c in stack:
            if c=='0':
                if nonZero:
                    s+=c
            else:
                nonZero=True
                s+=c
        if len(s)==0:
            s='0'
        return s
        

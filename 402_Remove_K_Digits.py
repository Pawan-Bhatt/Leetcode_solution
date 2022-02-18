class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for c in num:
            while len(stack)!=0 and k>0 and stack[len(stack)-1]>c:       # c is element of string if stack is not empty and number of element is greater then 0 and our pervious element is greater then remove current element  
                stack.pop()           # then we remove the greater element form the stack if we found it 
                k-=1                  # then our remaining element is -1
            stack.append(c)             # else we append the element in the satck 
        while k>0 and len(stack)!=0:     
            stack.pop()
            k-=1
        s=""
        nonZero=False
        for c in stack:                                               # this loop is for removuing zero form the string 
            if c=='0':
                if nonZero:
                    s+=c
            else:
                nonZero=True
                s+=c
        if len(s)==0:                               # if the length is zero then return 0
            s='0'
        return s
        

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if(i=='../'):
                if(stack):
                    stack.pop()
            elif(i=='./'):
                continue
            else:
                stack.append(i)
        return len(stack)
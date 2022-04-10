class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if(i=="../"):
                count-=1
            elif (i=="./" ):
                pass
            else :
                count +=1
            if count< 0 :
                count = 0
        return count
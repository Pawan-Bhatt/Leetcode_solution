class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key=len)
        dic = {}
        
        for i in words:
            dic[ i ] = 1
            
            for j in range(len(i)):
                
                # creating words by deleting a letter
                successor = i[:j] + i[j+1:]
                if successor in dic:
                    dic[ i ] = max (dic[i], 1 + dic[successor])
        
        res = max(dic.values())
        return res

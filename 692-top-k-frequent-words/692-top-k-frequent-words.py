class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordDict = {}
        for word in words:
            if word not in wordDict:
                wordDict[word] = 1;
            else:
                wordDict[word] += 1;

        sortedDict = sorted(wordDict.items(),key=lambda x: (-x[1],x[0]),reverse=False)
    
        trimedDict = (sortedDict[:k])
        result = []
        for i in range(k):
            result.append(trimedDict[i][0])
        return result
        
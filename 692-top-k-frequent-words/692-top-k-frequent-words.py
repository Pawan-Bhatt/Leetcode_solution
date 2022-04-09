class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_k = sorted(Counter(words).items(),key = lambda x:(-x[1],x[0]))
        return [words_k[x][0] for x in range(k)]
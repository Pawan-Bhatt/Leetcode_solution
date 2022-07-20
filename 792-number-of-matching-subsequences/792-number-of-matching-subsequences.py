class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ln = len(words)
        dct = defaultdict(list)
        wordLvls = [0]*ln
        
        for i, word in enumerate(words):
            dct[word[0]].append(i)
         
        ans = 0
        for c in s:
            if c not in dct:
                continue
            lst = dct.pop(c)
            for i in lst:
                wordLvls[i] += 1
                if wordLvls[i] < len(words[i]):
                    dct[words[i][wordLvls[i]]].append(i)
                else:
                    ans += 1
                        
        return ans
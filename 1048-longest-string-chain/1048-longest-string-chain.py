class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.wordsPresent = set(words)
        self.memo = {}
        reply = 0
        
        def dfs(word):
            if word in self.memo: return self.memo[word]
            maxLength = 1
            tmp = list(word)
            for i in range(len(word)):
                tmp.pop(i)
                a2s = ''.join(tmp)
                if a2s in self.wordsPresent:
                    length = 1 + dfs(a2s)
                    maxLength = max(length, maxLength)
                tmp.insert(i, word[i])
            self.memo[word] = maxLength
            return maxLength
        words.sort(key=len)
        for word in words[::-1]:
            reply = max(reply, dfs(word))
            if reply == len(word) - len(words[0]) + 1: break
        return reply
            
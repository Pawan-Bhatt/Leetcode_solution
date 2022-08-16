class Solution:
    def firstUniqChar(self, s: str) -> int:
        for a,b in Counter(s).items():
            if b==1:
                return s.index(a)
        return -1
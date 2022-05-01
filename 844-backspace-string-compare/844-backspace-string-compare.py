class Solution:
    def backspaceCompare(self, s, t):
        i, j = len(s), len(t)
        
        while i >= 0 and j >= 0:
            delete = 1
            while delete: i -= 1; delete += 1 if i >= 0 and s[i] == '#' else -1
            
            delete = 1
            while delete: j -= 1; delete += 1 if j >= 0 and t[j] == '#' else -1
                
            if i >= 0 and j >= 0 and s[i] != t[j]: return False
        
        return i < 0 and j < 0
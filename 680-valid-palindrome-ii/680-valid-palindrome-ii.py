class Solution(object):
    def validPalindrome(self, s):
        h, t = 0, len(s) - 1  # head and tail
        while h < t:
            if s[h] != s[t]:  # delete s[h] or s[t] and validate palindrome finally
                 return s[h:t] == s[h:t][::-1] or s[h + 1:t + 1] == s[h + 1:t + 1][::-1]
            h, t = h + 1, t - 1
        return True
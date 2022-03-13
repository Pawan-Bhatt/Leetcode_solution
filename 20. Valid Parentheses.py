class Solution:
    def isValid(self, s: str) -> bool:
        check = {")": "(", "}": "{", "]": "["}
        q = []
        for item in s:
            if item in check: 
                if q and q[-1] == check[item]:
                    q.pop()
                else:
                    return False
            else:
                q.append(item)
        if not q:
            return True
        else:
            return False

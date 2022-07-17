class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        j = 0
        for i in encoded:
            ans.append(i ^ ans[j])
            j += 1
        return ans
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for n in encoded:
            arr.append(arr[-1] ^ n) # getting XOR
        return arr
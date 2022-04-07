from sortedcontainers import SortedList

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sl = SortedList(stones)
        while len(sl) >= 2:
            y = sl.pop()
            x = sl.pop()
            if y > x:
                sl.add(y - x)
        return sl.pop() if len(sl) else 0
                
        
        
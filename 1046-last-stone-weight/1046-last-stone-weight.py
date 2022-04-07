from sortedcontainers import SortedList

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for idx in range(len(stones)):
            stones[idx] *= -1
        heapq.heapify(stones)

        while len(stones)>1:
            heavy_stone = heapq.heappop(stones)
            light_stone = heapq.heappop(stones)
            if heavy_stone != light_stone:
                heapq.heappush(stones, heavy_stone-light_stone)
            # print(stones)
        return -stones[0] if stones else 0
                
        
        
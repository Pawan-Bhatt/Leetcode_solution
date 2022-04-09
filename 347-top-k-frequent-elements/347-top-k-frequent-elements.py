class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections, heapq
        counter = collections.Counter(nums)
        pq = []
        nums = set(nums)
        
        for num in nums:
            cnt = counter[num]
            heapq.heappush(pq, (-cnt, num))
            
        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(pq)[1])
            
        return ret
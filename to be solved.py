Shortest Path Visiting All Nodes





class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        q = []
        distDic = defaultdict(lambda: math.inf)
        for nd in range(len(graph)):
            bm = 1 << nd
            q.append((0, -1, bm, nd))
            distDic[nd,bm] = 0
        G = (1 << len(graph))-1

        while q:
            repeat, num_nd, bitmask, nd = heapq.heappop(q)
            if bitmask == G:
                return len(graph)-1 + repeat
            dist_nd = distDic[nd,bitmask]
            for ch in graph[nd]:
                new_bm = bitmask | (1 << ch)
                if dist_nd+1 >= distDic[ch, new_bm]:
                    continue
                distDic[ch,new_bm] = dist_nd+1
                if (1 << ch) & bitmask > 0:
                    heapq.heappush(q, (repeat+1,num_nd,bitmask,ch))
                else:
                    heapq.heappush(q, (repeat, num_nd - 1, new_bm, ch))
        return -1

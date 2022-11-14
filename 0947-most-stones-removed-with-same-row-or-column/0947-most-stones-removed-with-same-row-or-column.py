class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        graphX = defaultdict(list)
        graphY = defaultdict(list)
        for x,y in stones:
            graphX[x].append(y)
            graphY[y].append(x)
        
        def dfs(xo,yo):
            nonlocal visited
            if (xo,yo) not in visited:
                visited.add((xo,yo))
                for neiY in graphX[xo]:
                    dfs(xo,neiY)
                for neiX in graphY[yo]:
                    dfs(neiX,yo)
        
        connectedComponent = 0
        visited = set()
        for x,y in stones:
            if (x,y) not in visited:
                dfs(x,y)
                connectedComponent += 1
        
        return len(stones)-connectedComponent
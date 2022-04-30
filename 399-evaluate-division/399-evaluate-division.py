class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def answer(curr: str, value: float) -> float:
            # required: self.graph, self.goal, self.seen
            if curr == self.goal:
                return value
            for adj, adj_value in self.graph[curr].items():
                if adj not in self.seen:
                    self.seen.add(adj)
                    result = answer(adj, value*adj_value)  # orig/adj = (orig/curr) * (curr/adj) = value*adj_value
                    if result != -1:
                        return result
                    self.seen.remove(adj)  # backtrack
            return -1
        
        self.graph = defaultdict(dict)
        self.seen = set()  # all visited expressions
        for (a, b), value in zip(equations, values):
            self.graph[a][b] = value  # a/b = value, given
            self.graph[b][a] = 1/value  # b/a = 1/(a/b) = 1/value
        result = []
        for orig, self.goal in queries:
            result.append(answer(orig, 1) if orig in self.graph else -1)
            self.seen.clear()
        return result
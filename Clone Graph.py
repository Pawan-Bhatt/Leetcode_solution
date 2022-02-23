"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
         # Edge Case
        if node is None:
            return None 
        graphMap = {}
        
        def dfs(node):
            if node in graphMap: 
                return graphMap[node]
            cloneNode = Node(node.val)
            graphMap[node] = cloneNode
            # Find neighbor
            for neighbor in node.neighbors:
                cloneNode.neighbors.append(dfs(neighbor))
            return cloneNode
        
        return dfs(node)
        

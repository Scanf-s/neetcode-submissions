"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_dict: dict['Node', 'Node'] = {}
        q: deque = deque()
        q.append(node)
        node_dict[node] = Node(val=node.val, neighbors=[])
        visited: set = set()
        visited.add(node)
        while q:
            cur: 'Node' = q.popleft()
            for n in cur.neighbors:
                if n not in visited:
                    node_dict[n] = Node(val=n.val, neighbors=[])
                    q.append(n)
                    visited.add(n)
                
                if node_dict[n] not in node_dict[cur].neighbors:
                    node_dict[cur].neighbors.append(node_dict[n])
                if node_dict[cur] not in node_dict[n].neighbors:
                    node_dict[n].neighbors.append(node_dict[cur])

        return node_dict[node]
        
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
        d = deque()
        d.append(node)
        conmap = {} ## og - > copy
        while d:
            curr = d.popleft()
            if curr:
                conmap[curr] = Node(curr.val)
                for neighbor in curr.neighbors:
                    if neighbor not in conmap:
                        d.append(neighbor)
        
        # at this point we have connection of different nodes 
        
        for original in conmap:
            copy = conmap[original]
            copyadj = copy.neighbors
            for neigh in original.neighbors:
                copyadj.append(conmap[neigh])
        
        if node:
            return conmap[node]
        return None
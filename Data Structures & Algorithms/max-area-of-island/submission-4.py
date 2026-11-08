from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def neighbors(curr):
            i = curr[0]
            j = curr[1]
            l1 = []
            if (i!=0):
                l1.append((i-1,j))
            if (i!=len(grid)-1):
                l1.append((i+1,j))
            if (j!=0):
                l1.append((i,j-1))
            if (j!=len(grid[0])-1):
                l1.append((i,j+1))
            return l1
        count = 0
        def bfs(i, j):
            count = 1
            d = deque()
            grid[i][j] = 0
            d.append((i,j))
            while d:
                curr = d.popleft()
                for neigh in neighbors(curr):
                    if grid[(neigh[0])][neigh[1]] == 1:
                        count +=1
                        d.append((neigh[0],neigh[1]))
                        grid[neigh[0]][neigh[1]] =0
            return count

        numislands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    
                    c = bfs(i,j)
                    count = max(count, c)
                    numislands +=1

        return count             
            
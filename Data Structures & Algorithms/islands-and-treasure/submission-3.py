class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF =  2147483647


        ## [ INF -1 0  INF     ] 
        ## [ INF INF INF -1    ]
        ## [ INF  -1 INF  -1   ]
        ## [ 0   -1   INF INF  ]
        

        # 3 -1 0 1
        # 2 2  1 -1 
        # 1 -1 2 -1
        # 0 -1 3 4
        
        def neighbors(x,y):
            l = []
            if x != 0:
                l.append((x-1,y))
            if x!=len(grid) - 1:
                l.append((x+1,y))

            if y!=0:
                l.append((x,y-1))
            if y!=len(grid[0]) - 1:
                l.append((x,y+1))

            return l

        d = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    d.append((i,j))
        
        
        while d:
            x,y = d.popleft()
            for n in neighbors(x,y):
                i, j = n
                if grid[i][j] == INF:
                    d.append((i,j))
                    grid[i][j] = grid[x][y] + 1
    

    






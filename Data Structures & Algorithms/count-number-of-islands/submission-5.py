class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        import heapq
        marked = set()
        heap = []
        num1 = 0
        count = 0
        currx = 0
        curry = 0
        numislands = 0
        
        for i in grid:
            for j in i:
                if j == "1":
                    num1+=1
        
        print(num1)

        def neighbors(i,j):
            list1 = []
            if i != 0:
                if grid[i-1][j] == "1":
                    list1.append([i-1,j])
            if i != len(grid) - 1:
                if grid[i+1][j] == "1":
                    list1.append([i+1,j])
            if j!=0:
                if grid[i][j-1] == "1":
                    list1.append([i,j-1])
            if j!=len(grid[0]) - 1:
                if grid[i][j+1] == "1":
                    list1.append([i,j+1])
            return list1

        def dimensionalize(i, j):
            return i*len(grid[0]) + j

        def bfs(i, j):
            nonlocal num1, numislands
    
                #onIsland = True
            marked.add(dimensionalize(i,j))
            if grid[i][j] == "1":
                num1-=1
                numislands +=1
                for pair in neighbors(i,j):
                    if dimensionalize(pair[0],pair[1]) not in marked:
                        heapq.heappush(heap, [pair[0],pair[1]])
                    marked.add(dimensionalize(pair[0],pair[1]))

                while len(heap) != 0 and num1 > 0:
                    curr = heapq.heappop(heap)
                    val = grid[curr[0]][curr[1]]
                    num1-=1
                    for pair in neighbors(curr[0],curr[1]):
                        if dimensionalize(pair[0],pair[1]) not in marked:
                            heapq.heappush(heap, [pair[0],pair[1]])
                            marked.add(dimensionalize(pair[0],pair[1]))
                    
        cond = True
        while num1 > 0 and grid[currx][curry] != "1":
            if curry != len(grid[0]) - 1:
                    curry +=1
            else:
                curry = 0
                if currx == len(grid) - 1:
                    cond = False
                    break
                currx+=1
        cond = True

        while num1 > 0 and cond:
            bfs(currx, curry)
            while dimensionalize(currx, curry) in marked:
                if curry != len(grid[0]) - 1:
                    curry +=1
                else:
                    curry = 0
                    if currx == len(grid) - 1:
                        cond = False
                        break
                    currx+=1
            


        return numislands
                        
                
                
                
                
                
                
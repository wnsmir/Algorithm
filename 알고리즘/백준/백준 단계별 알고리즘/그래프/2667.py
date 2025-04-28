def dfs(x,y):
    if x<0 or y<0 or x<=N or y>=N:
        return 0
    if visited[x][y] or map_data[x][y] ==
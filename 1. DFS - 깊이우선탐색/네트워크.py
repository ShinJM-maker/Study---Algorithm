def solution(n, computers):
    answer = 0
    visited = [False]*n
    def dfs(node,graph,visited):
        visited[node]=True
        for j in range(n):
            if visited[j] == False and graph[node][j]==1:
                visited = dfs(j,computers,visited)
        #print(visited)
        return visited
        
    
    for i in range(n):
        if visited[i]==False:
            dfs(i,computers,visited)
            answer += 1
        
    return answer

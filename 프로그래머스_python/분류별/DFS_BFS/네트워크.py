def dfs(graph,visit,x):
    
    start = x
    visit[x] = 1
    
    for i in graph[x]:
        if visit[i] != 1 :
            dfs(graph,visit,i)

    


def solution(n, computers):
    answer = 0
    
    graph = [[] for _ in range(n)]
    visit = [0] * n
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            
            elif computers[i][j] == 1:
                graph[i].append(j)
    
    for i in range(len(graph)):
        if visit[i] == 1:
            continue
        
        dfs(graph,visit,i)
        answer += 1
        
    
            
    
    
    
    
    
    
    return answer

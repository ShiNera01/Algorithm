import heapq

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    distance = [1e9] * (n + 1)
    count = 0
    start = 1
    max_value = 0
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist,here = heapq.heappop(q)
        
        if distance[here] < dist:
            continue
            
        for i in graph[here]:
            cost = dist + 1
            
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost,i))

        

    for i in range(1,n+1):
        if max_value < distance[i]:
            max_value = distance[i]
    
    for i in range(1,n+1):
        if max_value == distance[i]:
            count += 1
    
    answer = count
    return answer

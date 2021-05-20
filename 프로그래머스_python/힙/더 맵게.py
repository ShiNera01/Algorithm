import heapq

def solution(scoville, K):
    answer = 0
    
    q = []
    
    for i in scoville:
        heapq.heappush(q,i)
    
    if q[1] == 0:
        answer = -1
        return answer
    
    
    while q[0] < K:
        if len(q) < 2:
            answer = -1
            return answer
        
        result = heapq.heappop(q) + heapq.heappop(q) * 2
        heapq.heappush(q,result)
        answer += 1
    
    return answer

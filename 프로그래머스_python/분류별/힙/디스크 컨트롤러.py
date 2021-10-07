import heapq

def solution(jobs):
    answer = 0
    q = []
    time = 0
    size = len(jobs)
    count = 0    
    jobs_index = 0
    
    jobs.sort()
    
    while count < size:
        while jobs_index < size:
            if jobs[jobs_index][0] <= time:
                heapq.heappush(q,[jobs[jobs_index][1],jobs[jobs_index][0]])
                jobs_index += 1
            else:
                break
            
        if q:
            now = heapq.heappop(q)
            answer += time - now[1] + now[0]
            time += now[0]
            count += 1
            
        else:
            time = jobs[jobs_index][0]
            
    
    answer //= size
    return answer

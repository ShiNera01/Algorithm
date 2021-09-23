from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    q = deque()
    
    for i in range(len(progresses)):
        q.append(math.ceil((100 - progresses[i])/speeds[i]))
    
    start = q.popleft()
    
    count = 1
    
    while q:
        if start >= q[0]:
            count += 1
            q.popleft()
        else:
            answer.append(count)
            count = 1
            start = q.popleft()
    
    answer.append(count)
            
            
        
        
    return answer

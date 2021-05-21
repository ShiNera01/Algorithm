import heapq
from collections import deque 

def solution(priorities, location):
    answer = 0
    
    q = []
    priorities_q = deque()
    for i in range(len(priorities)):
        priorities_q.append((priorities[i], i))
        heapq.heappush(q,(-priorities[i]))

    count = 1

    
    while count <= len(priorities):

        if -priorities_q[0][0] == q[0]:
            if priorities_q[0][1] == location:
                answer = count
                break
            priorities_q.popleft()
            heapq.heappop(q)
            count += 1
        else:
            priorities_q.append(priorities_q[0])
            priorities_q.popleft()
            
    
    return answer

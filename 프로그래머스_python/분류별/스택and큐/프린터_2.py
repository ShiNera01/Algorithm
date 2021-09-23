from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque()
    
    for i in range(len(priorities)):
        q.append((i,priorities[i]))
    
    
    count = 1
    while q:
        max_value = max(priorities)
        
        if q[0][1] == max_value and q[0][0] == location:
            return count
            
        elif q[0][1] == max_value:
            q.popleft()
            priorities.remove(max_value)
            count += 1
        else:
            q.append(q.popleft())
    
    return answer

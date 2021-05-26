from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    queue = deque()
    time_cost = 0
    weight_cost = 0
    index = 0
    
    for i in range(bridge_length):
        queue.append(0)
    
    
    while index < len(truck_weights):
        
        weight_cost -= queue[0]
        queue.popleft()
        time_cost += 1
        
        if weight_cost + truck_weights[index] <= weight:
            queue.append(truck_weights[index])
            weight_cost += truck_weights[index]
            index += 1
        
        else:
            queue.append(0)
            
    while queue:
        queue.popleft()
        time_cost += 1
        
    answer = time_cost
    return answer

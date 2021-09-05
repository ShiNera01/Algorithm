def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    lost_copy = lost[:]
    
    
    for i in range(len(lost)):
        
        if lost[i] in reserve:
            lost_copy.remove(lost[i])
            reserve.remove(lost[i])
            
        elif (lost[i] - 1) in reserve:
            
            lost_copy.remove(lost[i])
            reserve.remove(lost[i] - 1)
            
        elif (lost[i] + 1) in reserve and (lost[i] + 1) not in lost:
            lost_copy.remove(lost[i])
            reserve.remove(lost[i] + 1)
            
            
        
    answer = n - len(lost_copy)
    
    return answer

def solution(n, lost, reserve):
    answer = 0
    
    number = 0
    
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = -1
    
    for i in range(len(lost)):
        if lost[i] - 1 in reserve:
            reserve.remove(lost[i] - 1)
            lost[i] = -1
            
        elif lost[i] + 1 in reserve:
            reserve.remove(lost[i] + 1)
            lost[i] = -1
    
    for i in range(len(lost)):
        if lost[i] != -1:
            number += 1
    
    answer = n - number
    return answer

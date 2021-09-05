import math

def solution(progresses, speeds):
    answer = []
    array = []
    
    for i in range(len(progresses)):
        array.append(100 - progresses[i])
    
    for i in range(len(array)):
        array[i] = math.ceil(array[i] / speeds[i])
        
    start = 0
    index = 0
    count = 0
    while index < len(array):
        if array[index] <= array[start]:
            index += 1
            count += 1
        else:
            answer.append(count)
            start = index
            count = 0
    
    if count != 0:
        answer.append(count)
            
    return answer

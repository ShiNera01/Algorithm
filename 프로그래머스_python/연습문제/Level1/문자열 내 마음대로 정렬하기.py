def solution(strings, n):
    answer = []
    
    array = sorted(strings, key = lambda x : (x[n],x))
    
    for i in range(len(array)):
        answer.append(array[i])
    
    return answer

def solution(n, costs):
    answer = 0
    
    only = set([])
    array = sorted(costs, key = lambda x:x[2])
    i = 0
    
    
        
        
    
    only.update([array[0][0], array[0][1]])
    answer += array[0][2]
    del array[0]
    
    while len(only) < n:
        if array[i][0] in only and array[i][1] in only:
            i += 1
        elif array[i][0] in only:
            only.add(array[i][1])
            answer += array[i][2]
            del array[i]
            i = 0
        elif array[i][1] in only:
            only.add(array[i][0])
            answer += array[i][2]
            del array[i]
            i = 0
        else:
            i += 1
            

        
    
    
    return answer

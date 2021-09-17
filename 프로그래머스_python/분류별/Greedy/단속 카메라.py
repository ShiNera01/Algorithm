def solution(routes):
    answer = 0
    
    routes = sorted(routes, key = lambda x : (x[0],x[1]))
    
    left, right = 0,0
    
    while right < len(routes):
        
        for i in range(left,right + 1):
            if routes[i][0] <= routes[right][0] <= routes[i][1]:
                pass
            else:
                
                answer += 1
                left = right
                break
            

        right += 1
    
    answer += 1
        
    
    return answer

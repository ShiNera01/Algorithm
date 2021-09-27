def solution(sizes):
    answer = 0
    
    max_garo = 0
    max_sero = 0
    temp = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][1]
            sizes[i][1] = sizes[i][0]
            sizes[i][0] = temp
            
        if sizes[i][0] > max_garo:
            max_garo = sizes[i][0]
            
        if sizes[i][1] > max_sero:
            max_sero = sizes[i][1]
        
    
    answer = max_garo * max_sero
    
    return answer

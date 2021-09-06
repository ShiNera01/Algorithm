def solution(weights, head2head):
    answer = [i+1 for i in range(len(weights))]
    win_rate = []
    more_weight = [0 for i in range(len(weights))]
    array = [[0] * len(weights) for _ in range(len(weights))]
    
    for i in range(len(weights)):
        for j in range(len(weights)):
            if head2head[i][j] == "W":
                array[i][j] = 1
            elif head2head[i][j] == "L":
                array[i][j] = -1
            else:
                array[i][j] = 0
    
    for i in range(len(weights)):
        
        if (head2head[i].count("W") + head2head[i].count("L")) == 0:
            win_rate.append(0)
        else:
            win_rate.append(head2head[i].count("W")/(head2head[i].count("W") + head2head[i].count("L")))
            
    
    for i in range(len(weights)):
        for j in range(len(head2head[i])):
            if head2head[i][j] == "W" and weights[i] < weights[j]:
                more_weight[i] += 1
                
    
    
    answer = sorted(answer, key = lambda x : (-win_rate[x-1], -more_weight[x-1], -weights[x-1],x-1))
    
    
    
    
    
    return answer

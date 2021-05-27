def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            width = yellow // i
            height = i
        else :
            continue
        
        if (width + 2) * (height + 2) == brown + yellow:
            answer.append(width + 2)
            answer.append(height + 2)
            break
    
    return answer

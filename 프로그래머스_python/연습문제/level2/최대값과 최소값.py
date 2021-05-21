def solution(s):
    answer = ''
    
    number = list(map(int,s.split()))
    max_value = number[0]
    min_value = number[0]
    
    
    for i in number:
        if i > max_value:
            max_value = i
        
        if i < min_value:
            min_value = i
    answer += str(min_value) + ' ' + str(max_value)
    
    
    return answer

def solution(n):
    answer = 0
    
    array = []
    
    while (n > 0):
        
        array.append(n%10)
        n //= 10
    
    array = sorted(array,reverse = True)
    
    for i in range(len(array)):
        answer = answer * 10 + array[i]
        
    
    return answer

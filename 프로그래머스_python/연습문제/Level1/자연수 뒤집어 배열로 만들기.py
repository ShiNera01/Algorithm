def solution(n):
    answer = []
    array = []
    
    while(n > 0):
        array.append(n%10)
        n = n//10
    
    
    answer = array[:]
    
    return answer

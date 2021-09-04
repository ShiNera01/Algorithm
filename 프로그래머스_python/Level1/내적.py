def solution(a, b):
    answer = 1234567890
    
    array = list(map(lambda x,y : x * y, a,b))
    answer = sum(array)
    
    return answer

import math

def solution(n):
    answer = 0
    
    if int(math.sqrt(n)) != int(math.ceil(math.sqrt(n))):
        answer = -1
    else:
        answer = pow(math.sqrt(n) + 1,2)
    
    return answer

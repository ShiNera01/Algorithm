def solution(x):
    
    
    number = x
    total = 0
    
    while number > 0:
        total = total + number % 10
        number = number // 10
    
    if x % total == 0:
        answer = True
    else:
        answer = False
    
    return answer

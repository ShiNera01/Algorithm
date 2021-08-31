def solution(price, money, count):
    answer = -1
    
    cost = 0
    
    for i in range(1, count + 1):
        cost += price * i
    
    if money >= cost:
        answer = 0
    else :
        answer = cost - money
    

    return answer

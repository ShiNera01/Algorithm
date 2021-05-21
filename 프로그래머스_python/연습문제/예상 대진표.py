def solution(n,a,b):
    answer = 0

    a = a - 1
    b = b - 1
    
    
    while a != b:
        a = a // 2
        b = b // 2
        answer += 1
        if a == b:
            break
    


    return answer

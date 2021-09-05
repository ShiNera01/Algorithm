def solution(n):
    answer = ''
    
    array = ["수","박"]
    
    for i in range(n):
        if i % 2 == 0:
            answer += array[0]
        else:
            answer += array[1]
    
    return answer

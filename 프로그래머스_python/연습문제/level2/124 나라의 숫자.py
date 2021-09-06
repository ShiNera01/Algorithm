def solution(n):
    answer = ''
    
    number = n
    
    while number != 0:
        number_2 = number % 3
        if number_2 == 0:
            number = number // 3 - 1
        else:
            number = number // 3
        
        if number_2 == 1:
            answer += str(1)
        elif number_2 == 2:
            answer += str(2)
        else :
            answer += str(4)
    
    answer = answer[::-1]
    
    return answer

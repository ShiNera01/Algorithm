import math

def solution(n):
    answer = 0
    number = n
    array = []
    
    while True:
        if(number < 3):
            array.append(number)
            break
        array.append(number % 3)
        number = number // 3
    
    
    for i in range(1, len(array) + 1):
        answer += math.pow(3, len(array) - i) * array[i - 1]
    
    
    return answer

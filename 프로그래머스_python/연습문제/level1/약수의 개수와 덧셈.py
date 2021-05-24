import math

def perfect_square(number):
    
    array = []
    
    for i in range(1,number + 1):
        if number % i == 0:
            array.append(i)
    
    return len(array)

def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        if perfect_square(i) % 2 == 0:
            answer += i
        else : 
            answer -= i
    
    
    return answer

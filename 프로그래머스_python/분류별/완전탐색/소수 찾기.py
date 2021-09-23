from itertools import permutations
import math

def is_prime(number):
    if number == 0 or number == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(number) + 1)):
            if number % i == 0:
                return False
            
    return True

def solution(numbers):
    answer = 0
    
    array = list(numbers)
    array_total = []
    
    for i in range(1, len(array) + 1):
        array_per = list(map(''.join,permutations(array,i)))
        array_total += array_per
    
    for i in range(len(array_total)):
        array_total[i] = int(array_total[i])
    
    
    array_total = set(array_total)
    array_total = list(array_total)
    
    for i in range(len(array_total)):
        if is_prime(array_total[i]) == True:
            answer += 1
            
    
    return answer

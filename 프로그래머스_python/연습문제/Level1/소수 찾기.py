import math

def prime_number(number):
    
    array = [1 for i in range(number + 1)]
    
    array[1] = 0
    count = 0
    
    for i in range(2, int(math.sqrt(number)) + 1):
        j = 2
        while i * j <= number:
            array[i*j] = 0
            j += 1
    
    for i in range(1,number + 1):
        if array[i] == 1:
            count += 1
    
    return count

def solution(n):
    answer = 0
    
    answer = prime_number(n)
    
    return answer

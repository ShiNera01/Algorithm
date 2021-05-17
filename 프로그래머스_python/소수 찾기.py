from itertools import permutations
import math

def isprime(number):
    if number == 1  or number == 0: 
        return False

    for i in range(2 , int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
        
    return True


def solution(numbers):
    answer = 0
    result = []
    for i in range (1,len(numbers) + 1):
        result += (list(map(''.join, permutations(numbers, i))))
    
    result = list(set(result))
    
    result = [i for i in result if not i.startswith('0')]
    
    for i in result:
        if isprime(int(i)):
            answer += 1
            print(i)
        else :
            continue
    
    return answer

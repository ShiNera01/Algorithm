from itertools import combinations
import math

def is_prime(number):
    
    if number == 1:
        return False
    
    flag = True
    for i in range(2,int(math.sqrt(number)) + 1):
        if number % i == 0:
            flag = False
            break
            
    return flag
    
def solution(nums):
    answer = 0

    array = list(combinations(nums,3))
    array_sum = []
    
    for i in range(len(array)):
        array_sum.append(array[i][0] + array[i][1] + array[i][2])
    
    
    
    
    for i in array_sum:
        if is_prime(i) == True:
            
            answer += 1
    
    
    

    return answer

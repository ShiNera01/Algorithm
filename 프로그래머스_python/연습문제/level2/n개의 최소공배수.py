import math

def lcd(a,b):
    number = a * b // math.gcd(a,b)
    return number


def solution(arr):
    answer = 0
    answer = 1
    for i in range(len(arr)):
        answer = lcd(answer,arr[i])
        
    
    return answer

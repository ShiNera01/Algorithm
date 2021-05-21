def solution(n):
    ans = 0
    
    number = n
    while number > 0:
        if number % 2 == 0:
            number = number // 2
        else :
            number -= 1
            ans += 1
        
        

    return ans

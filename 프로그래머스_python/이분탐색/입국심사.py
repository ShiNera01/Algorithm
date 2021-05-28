def solution(n, times):
    answer = 0
    
    left = 1
    right = max(times) * n
    
    
    while left <= right:
        mid = (left + right) // 2
        number = 0
        for i in times:
            number += mid // i
        
        if number >= n :
            answer = mid
            right = mid - 1
        
        elif number < n:
            left = mid + 1
            

        
    return answer

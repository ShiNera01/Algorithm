def solution(people, limit):
    answer = 0
    
    people.sort(reverse = True)
    
    left = 0
    right = len(people) - 1
    
    while left <= right:
        
        if left == right:
            answer += 1
            break
        
        elif people[left] + people[right] > limit:
            answer += 1
            left += 1
        else :
            answer += 1
            left += 1
            right -= 1
    
    return answer

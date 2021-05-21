def solution(n):
    answer = 0
    
    numbers = [0]
    
    if n % 2 == 0:
        for i in range(1,n//2 + 1):
            numbers.append(numbers[-1] + i)
    else :
        for i in range(1, n//2 + 2):
            numbers.append(numbers[-1] + i)
    left = 0
    right = left + 1
    print(numbers)
    while left < len(numbers) and right <len(numbers):
        number = numbers[right] - numbers[left]
        
        if number == n:
            answer += 1
            left += 1
            right += 1
            
    
        elif number < n:
            right += 1
        else :
            left += 1
    answer += 1
    return answer

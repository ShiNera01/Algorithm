def solution(nums):
    answer = 0
    
    number = len(nums)/2
    
    array = set()
    
    for i in nums:
        array.add(i)
    
    answer = min(len(array), number)
    
    
    
    return answer

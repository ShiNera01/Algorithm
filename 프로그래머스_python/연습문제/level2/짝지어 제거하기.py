def solution(s):
    answer = 0
    
    if len(s) % 2 != 0:
        return 0
    
    array = list(s)
    stack = []
    count = 0
    
    for i in array:
        
        if len(stack) == 0:
            stack.append(i)
            
        elif i == stack[-1]:
            stack.pop()
            count += 1
            
        else:
            stack.append(i)
        
        
    if count == len(array)//2:
        answer = 1
        
    

    return answer

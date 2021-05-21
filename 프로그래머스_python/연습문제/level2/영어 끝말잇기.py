def solution(n, words):
    answer = []
    
    array = []
    
    count = 0
    order = 0
    last = ''
    for i in range(len(words)):
        
        if last != words[i][0] and len(array) != 0:
            order = (i + 1) % n
            count = (i // n) + 1
            if order == 0:
                order = n
            break
        
        elif words[i] in array:
            order = (i + 1) % n
            count = (i // n) + 1
            if order == 0:
                order = n
            break
        else :
            array.append(words[i])
            last = words[i][-1]
        
        
    
        
    answer.append(order)
    answer.append(count)
    return answer

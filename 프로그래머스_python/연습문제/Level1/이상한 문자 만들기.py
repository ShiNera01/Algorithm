def solution(s):
    answer = ''
    
    array = s.split(" ")
    result = []
    
    for i in array:
        word = ''
        for j in range(len(i)):
            
            if j % 2 == 0:
                word += i[j].upper()
            else:
                word += i[j].lower()
                
        result.append(word)
        
    answer = ' '.join(result)
    
    return answer

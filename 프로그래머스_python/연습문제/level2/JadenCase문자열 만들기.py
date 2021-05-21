def solution(s):
    answer = ''

    
    s = s.lower()
    
    if len(s) == 1:
        answer = s.upper()
        return answer 

    
    index = 0
    while index < len(s):
        
        if s[index] == ' ':
            for i in range(index,len(s)):
                if s[i] == ' ':
                    answer += s[i]
                else:
                    index = i
                    break
                if i == len(s) - 1:
                    index = len(s)
        else :
            answer += s[index].upper()
            for i in range(index + 1,len(s)):
                if s[i] == ' ':
                    index = i
                    break
                else:
                    answer += s[i]
                
                if i == len(s) - 1:
                    index = len(s)
            

        
        
    return answer

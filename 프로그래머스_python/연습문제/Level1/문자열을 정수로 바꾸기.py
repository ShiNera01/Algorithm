def solution(s):
    answer = 0
    
    flag = True
    length = len(s)
    if s[0] == '-':
        flag = False
    else:
        flag = True
        
    for i in s:
        if i.isdigit() == False:
            length -= 1
            continue
        else:
            answer += int(i) * pow(10,length-1)
            length -= 1
    
    if flag == False:
        answer *= -1
    
    return answer

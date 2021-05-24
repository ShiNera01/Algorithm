def solution(dartResult):
    answer = 0
    
    array = []
    number = 0
    
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            if dartResult[i] == 'S':
                number = number
                
            elif dartResult[i] == 'D':
                number = number * number
            else :
                number = number * number * number
            
            array.append(number)
        
        elif dartResult[i].isdigit():
            if dartResult[i] == '1':
                if dartResult[i+1] == '0':
                    continue
                else:
                    number = int(dartResult[i])
            elif dartResult[i] == '0':
                if dartResult[i-1] == '1':
                    number = int(dartResult[i-1] + dartResult[i])
                else:
                    number = int(dartResult[i])
            else:
                number = int(dartResult[i])
        else:
            if dartResult[i] == '#':
                array[-1] = array[-1] * -1
            elif dartResult[i] == '*':
                if len(array) >= 2:
                    for j in range(len(array)-2,len(array)):
                        array[j] = array[j] * 2
                else:
                    array[0] = array[0] * 2
    
    for i in array:
        answer += i
    
    return answer

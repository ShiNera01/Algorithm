def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        array_temp = []
        
        for j in range(commands[i][0] - 1, commands[i][1]):
            array_temp.append(array[j])
            array_temp.sort()
            
            
        answer.append(array_temp[commands[i][2] - 1])    
        
    return answer

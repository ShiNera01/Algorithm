def solution(s):
    answer = []
    
    array = []
    number = 0
    flag = 0
    
    for i in range(1,len(s)-1):
        
        if s[i] == "{":
            number_list = []
            flag = 1
            
        elif s[i].isdigit():
            number = number * 10 + int(s[i])
        
        elif s[i] == "," and flag == 1:
            number_list.append(number)
            number = 0
            
        elif s[i] == "}":
            number_list.append(number)
            array.append(number_list)
            number = 0
            flag = 0
        
        
    array = sorted(array, key = lambda x : len(x))
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] not in answer:
                answer.append(array[i][j])
    
    
    return answer

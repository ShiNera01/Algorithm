def solution(str1, str2):
    answer = 0
    
    array_1_final = list(str1)
    array_2_final = list(str2)
    
    array_1 = []
    array_2 = []
    
    
    
    for i in range(len(array_1_final) - 1):
        array_1.append(''.join(array_1_final[i:i+2]))
    for i in range(len(array_2_final) - 1):
        array_2.append(''.join(array_2_final[i:i+2]))
    
    
    array_1_final = []
    array_2_final = []
    
    
        
    for i in range(len(array_1)):
        if array_1[i].isalpha() == True:
            array_1_final.append(array_1[i].lower())
    
    for i in range(len(array_2)):
        if array_2[i].isalpha() == True:
            array_2_final.append(array_2[i].lower())
    

    if len(array_1_final) == 0 and len(array_2_final) == 0:
        return 65536
    
    array_1 = array_1_final
    array_2 = array_2_final

    
    common = []
    total = array_1_final + array_2_final
    
    if len(array_1_final) <= len(array_2_final):
        for i in range(len(array_1_final)):
            if array_1_final[i] in array_2:
                common.append(array_1_final[i])
                array_2.remove(array_1_final[i])
            
    else:
        for i in range(len(array_2_final)):
            if array_2_final[i] in array_1:
                common.append(array_2_final[i])
                array_1.remove(array_2_final[i])
    
    for i in range(len(common)):
        total.remove(common[i])
    
    
    result = len(common)/len(total) * 65536
    
    answer = int(result)
    
    
    
    return answer

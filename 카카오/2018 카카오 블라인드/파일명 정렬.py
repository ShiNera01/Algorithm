def solution(files):
    answer = []
    
    array = []
    
    
    
    for i in range(len(files)):
        word_list = []
        word_1 = ""
        word_2 = ""
        word_3 = ""
        flag_1 = 0
        flag_2 = 0
        for j in range(len(files[i])):
            
            if files[i][j].isdigit() != True and flag_1 == 0:
                word_1 += files[i][j]
            elif files[i][j].isdigit() == True and flag_2 == 0:
                word_2 += files[i][j]
                flag_1 = 1
            else:
                word_3 += files[i][j]
                flag_2 = 1
            
        word_list.append(word_1.lower())
        word_list.append(int(word_2))
        word_list.append(word_3)
        word_list.append(i)
    
        array.append(word_list)           
    
    array = sorted(array, key = lambda x: (x[0],x[1],x[3]))
    
    
    
    for i in range(len(array)):
        answer.append(files[array[i][3]])
    
    
    return answer

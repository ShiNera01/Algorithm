def solution(table, languages, preference):
    answer = ''
    max_value = 0
    
    for i in range(len(table)):
        array = table[i].split(' ')
        
        score = 0
        for j in range(len(languages)):
            word_index = 6
            if languages[j] in array:
                word_index = array.index(languages[j])
                score += preference[j] * abs(6 - word_index)
            else:
                continue
        
        if max_value < score:
            max_value = score
            answer = array[0]

        elif max_value == score and answer == ' ':
            answer = array[0]
            
        elif max_value == score and answer > array[0]:
            answer = array[0]
            
    return answer

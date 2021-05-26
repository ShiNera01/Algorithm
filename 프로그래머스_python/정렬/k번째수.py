def solution(array, commands):
    answer = []
    
    for i in commands:
        word = array[i[0]-1:i[1]]
        word.sort()
        answer.append(word[i[2] - 1])
        
    return answer

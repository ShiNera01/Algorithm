def solution(answers):
    answer = []
    
    array_1 = [1,2,3,4,5]
    array_2 = [2,1,2,3,2,4,2,5]
    array_3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer_number = [0,0,0]
    
    for i in range(len(answers)):
        if i >= len(array_1):
            index_1 = i % len(array_1)
        else:
            index_1 = i
        if answers[i] == array_1[index_1]:
            answer_number[0] += 1
            
        if i >= len(array_2):
            index_2 = i % len(array_2)
        else:
            index_2 = i
        if answers[i] == array_2[index_2]:
            answer_number[1] += 1
            
        if i >= len(array_3):
            index_3 = i % len(array_3)
        else:
            index_3 = i
        if answers[i] == array_3[index_3]:
            answer_number[2] += 1
    
    
    for i in range(len(answer_number)):
        if answer_number[i] == max(answer_number):
            answer.append(i + 1)
    
    return answer

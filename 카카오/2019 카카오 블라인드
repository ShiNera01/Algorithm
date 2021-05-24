from fractions import Fraction

def solution(N, stages):
    answer = []
    array = {0:0}
    number = len(stages)
    
    for i in range (1, N + 1):
        
        if number == 0:
            array[i] = 0
            continue
        count = 0
        
        for j in stages:
            if i == j:
                count += 1
        array[i] = Fraction(count,number)
        number -= count
    del array[0]
    answer_list = sorted(array.items(), key = lambda x:x[1],reverse = True)
    
    for i in answer_list:
        answer.append(i[0])
    
    return answer

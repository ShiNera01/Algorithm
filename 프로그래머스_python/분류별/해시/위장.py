def solution(clothes):
    answer = 0
    dict = {}
    
    for i in clothes:
        if i[1] in dict:
            dict[i[1]].append(i[0])
            
        else:
            dict[i[1]] = []
            dict[i[1]].append(i[0])
    
    answer += 1
    for i in dict.keys():
        answer *= (len(dict[i])) + 1
    answer -= 1
    return answer

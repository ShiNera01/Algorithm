def solution(skill, skill_trees):
    answer = 0
    
    result = True
    
    for word in skill_trees:
        result = True
        words = []
        for i in word:
            if i in skill:
                words.append(i)
        for i in range(len(words)):
            if skill[i] == words[i]:
                continue
            else:
                result = False
                break
        if result == False:
            continue
        else:
            answer += 1
    return answer

from collections import deque

def difference(a,b):
    result = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1
            
    return result
    

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    dic = dict()
    
    for i in range(len(words)):
        if difference(begin,words[i]) == 1 and begin not in dic:
            dic[begin] = [words[i]]
        elif difference(begin,words[i]) == 1:
            dic[begin].append(words[i])
    
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            elif difference(words[i],words[j]) == 1 and words[i] not in dic:
                dic[words[i]] = [words[j]]
            elif difference(words[i],words[j]) == 1:
                dic[words[i]].append(words[j])
    
    q = deque()
    index = 0
    q.append([begin,index])
    visit = []
    
    
    while q:
        word,index = q.popleft()
        
        
        if word == target:
            answer = index
        else:
            for i in (dic[word]):
                
                if i in visit:
                    continue
                
                q.append([i,index+1])
                visit.append(i)
    
    return answer

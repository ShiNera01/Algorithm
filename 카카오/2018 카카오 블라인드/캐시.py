def solution(cacheSize, cities):
    answer = 0
    
    array = []
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    
    for i in cities:
        if i in array:
            array.remove(i)
            array.append(i)
            answer += 1
            
        else:
            if cacheSize == 0:
                answer += 5
            elif len(array) == cacheSize:
                array.pop(0)
                array.append(i)
                answer += 5
            else:
                array.append(i)
                answer += 5
    
    
    return answer

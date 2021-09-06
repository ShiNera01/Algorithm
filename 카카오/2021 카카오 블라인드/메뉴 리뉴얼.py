from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in course:
        array_total = []
        for j in range(len(orders)):
            array = list(orders[j])
            array.sort()
            array = list(map(''.join,combinations(array,i)))
            print(array)
            
            array_total += array
            
        
        if len(array_total) == 0:
            continue
        
        max_count = array_total.count(max(array_total, key = array_total.count))
        
        
        if max_count < 2:
            continue
        
        s = set()
        for j in array_total:
            if max_count == array_total.count(j):
                s.add(j)
                
        
        answer += list(s)
        
    answer.sort()
        
    
    
    return answer

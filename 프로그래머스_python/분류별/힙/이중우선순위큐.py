import heapq

def solution(operations):
    answer = []
    
    min_heap = []
    
    for i in range(len(operations)):
        word = operations[i].split(" ")
        if word[0] == "I":
            heapq.heappush(min_heap, int(word[1]))
        
        elif len(min_heap) == 0:
            continue
        
        
        elif word[0] == "D" and word[1] == "1":
            del min_heap[min_heap.index(heapq.nlargest(1,min_heap)[0])]
            
        else:
            
            heapq.heappop(min_heap)
        
        
    
    if not min_heap:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(max(min_heap))
        answer.append(heapq.heappop(min_heap))
    
    return answer

def solution(prices):
    answer = [0] * len(prices)
    
    array = []
    
    i = 0
    
    while i < len(prices):

        if len(array) == 0:
            array.append(i)
            i += 1
        elif prices[array[-1]] <= prices[i]:
            array.append(i)
            i += 1
        else:
            answer[array[-1]] = i - array[-1]
            del array[-1]
    
    for i in array:
        answer[i] = len(prices) - 1 - i
    return answer

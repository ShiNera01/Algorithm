def solution(number, k):
    answer=''
    array = list(number)
    max_value = 0
    size = len(array)
    count = size - k
    index = 0
    
    for i in range(count):
        max_value = -1
        for j in range(index, size - count + i + 1):
            if array[j] == '9':
                max_value = int(array[j])
                index = j + 1
                break
            if max_value < int(array[j]):
                max_value = int(array[j])
                index = j + 1
        answer += str(max_value)
                
        

    
    return answer

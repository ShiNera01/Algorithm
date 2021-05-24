def binary_change(number,n):
    array = []
    
    while number >= 2:
        array.append(number % 2)
        number = number // 2
    array.append(number)
    
    
    while len(array) < n:
        array.append(0)
        
    array.reverse()
    return array

def solution(n, arr1, arr2):
    answer = []
    
    square = [[] * i for i in range(n)]
    
    for i in range(n):
        list_1 = binary_change(arr1[i],n)
        list_2 = binary_change(arr2[i],n)
        
        for j in range(n):
            if list_1[j] + list_2[j] >= 1:
                square[i].append(1)
            else : 
                square[i].append(0)
    
    for i in range(n):
        word = ''
        for j in range(n):
            if square[i][j] == 1:
                word += '#'
            else:
                word += ' '
        answer.append(word)
    return answer

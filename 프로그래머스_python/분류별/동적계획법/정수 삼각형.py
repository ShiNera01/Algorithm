def solve(array):
     
    
    for i in range(1, len(array)):
        for j in range(i + 1):
            if j == 0:
                array[i][0] += array[i - 1][0]
            elif j == i:
                array[i][j] += array[i - 1][i - 1]
            else :
                array[i][j] += max(array[i - 1][j - 1],array[i - 1][j])
    
    return array
    
def solution(triangle):
    answer = 0

    array = solve(triangle)

    for i in range(len(triangle)):
        if answer < array[len(triangle) - 1][i]:
            answer = array[len(triangle) -1][i]
    
    
    return answer

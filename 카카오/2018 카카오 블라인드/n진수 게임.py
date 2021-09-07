def change(n,number):
    
    result = ""
    
    if number < n:
        if number == 10:
            result = "A"
        elif number == 11:
            result = "B"
        elif number == 12:
            result = "C"
        elif number == 13:
            result = "D"
        elif number == 14:
            result = "E"
        elif number == 15:
            result = "F"
        else:
            result = str(number)
            
        return str(result)
    
    while number >= n:
        remainder = number % n
        number = number // n
        
        
        if remainder == 10:
            result = "A" + result
        elif remainder == 11:
            result = "B" + result
        elif remainder == 12:
            result = "C" + result
        elif remainder == 13:
            result = "D" + result
        elif remainder == 14:
            result = "E" + result
        elif remainder == 15:
            result = "F" + result
        else:
            result = str(remainder) + result
    
    if number == 10:
        result = "A" + result
    elif number == 11:
        result = "B" + result
    elif number == 12:
        result = "C" + result
    elif number == 13:
        result = "D" + result
    elif number == 14:
        result = "E" + result
    elif number == 15:
        result = "F" + result
    else:
        result = str(number) + result
    
    
    
    return result

def solution(n, t, m, p):
    answer = ''
    
    array = []
    index = 0
    
    while len(array) <= m * t:
        number_word = change(n,index)          # m * t 수 까지 숫자 선택하여 해당 진법으로 바꿔줌 change는 str리턴
        for j in range(len(number_word)):
            array.append(number_word[j])
        index += 1
    array = array[:m*t]
    
    
    for i in range(m*t):
        if i % m == p - 1:
            answer += array[i]
        

        
    return answer

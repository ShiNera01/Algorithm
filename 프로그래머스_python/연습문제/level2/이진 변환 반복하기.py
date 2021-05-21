def solution(s):
    answer = []
    
    word = s
    count = 0
    count_zero = 0
    
    while word != '1':
        new_word = ''
        for i in word:
            if i == '0':
                count_zero += 1
            else:
                new_word += i
        
        number = len(new_word)
        word = ''
        while number >= 2:
            word += str(number % 2)
            number = number // 2
        word += str(number)
        
        word = word[::-1]
        count += 1
        
    answer.append(count)
    answer.append(count_zero)
    return answer

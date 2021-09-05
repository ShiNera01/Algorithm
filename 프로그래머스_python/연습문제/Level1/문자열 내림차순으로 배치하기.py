def solution(s):
    answer = ''
    
    upper_array = []
    lower_array = []
    
    for i in range(len(s)):
        if s[i].isupper() == True:
            upper_array.append(s[i])
        else:
            lower_array.append(s[i])
    
    upper_array.sort(reverse = True)
    lower_array.sort(reverse = True)
    
    upper_array = ''.join(upper_array)
    lower_array = ''.join(lower_array)
    
    answer = lower_array + upper_array
    
    
    return answer

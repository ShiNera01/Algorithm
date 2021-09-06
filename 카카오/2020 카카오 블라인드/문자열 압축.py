
def solution(s):
    answer = len(s)

    
    
    
    
    
    for i in range(1, int(len(s)/2) + 1):
        index = 0
        word = ""
        comp_word = ""
        comp_word = s[index:index+i]
        
        count = 0
        
        while index + i <= len(s):
            
            while index + i <= len(s):
                if s[index : index + i] == comp_word:
                    index += i
                    count += 1
                else:
                    break
                
            if len(word) == 0 and count == 1:
                word += comp_word
            elif len(word) == 0 and count != 1:
                word += str(count) + comp_word
            elif count == 1:
                word = word + comp_word
            else:
                word = word + str(count) + comp_word
            
            comp_word = s[index:index+i]
            count = 0
            
        
        if index < len(s):
            word += s[index:]
            
        
        answer = min(answer,len(word))
        
    return answer

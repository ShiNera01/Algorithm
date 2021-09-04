def solution(new_id):
    answer = ''
    index = 0
    
    #step 1
    word = new_id.lower()
    
    #step 2
    for i in range(len(word)):
        if word[i].isalnum() or word[i] == '-' or word[i] == '_' or word[i] == '.':
            answer += word[i]
    
    word = answer
    answer = ''
    
    #step 3
    subword = ''
    while(index < len(word)):
        if word[index] == '.':
            subword = '.' 
        else :
            answer += subword + word[index]
            subword = ''
            
        index += 1
    if len(subword) != 0:
        answer += subword
        
    word = answer
    answer = ''
        
    #step 4
    if word.startswith('.') == True:
        word = word[1:len(word)]
    if word.endswith('.') == True:
        word = word[0:len(word) - 1]
        
    if len(word) == 0:
        word += 'a'
    #step 6
    if len(word) >= 16:
        word = word[:15]
    if word.endswith('.') == True:
        word = word[:len(word) - 1]
        
    #step 7
    while len(word) <= 2:
        word += word[len(word) - 1]
    
    answer = word
    return answer

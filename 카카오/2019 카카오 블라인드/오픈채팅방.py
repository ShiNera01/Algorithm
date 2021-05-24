def solution(record):
    answer = []
    
    record_id = {}
    
    for i in record:
        word = i.split(" ")
        
        if word[0] == "Enter" or word[0] == 'Change':
            record_id[word[1]] = word[2]
    
    for i in record:
        word = i.split(' ')
        
        if word[0] == 'Enter':
            answer.append(record_id[word[1]]+"님이 들어왔습니다.")
        elif word[0] == 'Leave':
            answer.append(record_id[word[1]]+"님이 나갔습니다.")
    
    return answer

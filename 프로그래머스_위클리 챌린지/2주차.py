def solution(scores):
    answer = ''
    
    for i in range(len(scores)):
        total_score = 0
        min_score, max_score = 101,-1
        count = len(scores)
        max_count,min_count = 0,0
        
        
        for j in range(len(scores[i])):
            total_score += scores[j][i]
            if min_score >= scores[j][i]:
                min_score = scores[j][i]
                
                
            if max_score <= scores[j][i]:
                max_score = scores[j][i] 
                
        for j in range(len(scores[i])):
            if scores[j][i] == min_score:
                min_count += 1
            if scores[j][i] == max_score:
                max_count += 1
        
        
        if max_score == scores[i][i] and max_count == 1:
            count -= 1
            total_score = (total_score - max_score)/count
            
        elif min_score == scores[i][i] and min_count == 1:
            count -= 1
            
            total_score = (total_score - min_score)/count
            
        else:
            total_score /= count
        
        if total_score >= 90:
            answer += 'A'
        elif 80 <= total_score < 90:
            answer += 'B'
        elif 70 <= total_score < 80:
            answer += 'C'
        elif 50 <= total_score < 70:
            answer += 'D'
        else:
            answer += 'F'
        
    return answer

def solution(lottos, win_nums):
    answer = []
    
    zero_count = 0
    count = 0
    for i in lottos:
        if i in win_nums:
            win_nums.remove(i)
            count += 1
        elif i == 0:
            zero_count += 1
    
    if count == 0 or count == 1:
        answer.append(min(7 - zero_count - count,6))
        answer.append(min(7 - count,6))
        
    else:
        answer.append(7 - count - zero_count)
        answer.append(7 - count)
    
    
    return answer

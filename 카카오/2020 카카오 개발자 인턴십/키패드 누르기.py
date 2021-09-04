def solution(numbers, hand):
    answer = ''
    
    #왼손 오른손 현재 위치
    left_position = [-1,3]
    right_position = [1,3]
    
    
    
    for i in numbers:
        
        
        if i == 1 or i == 4 or i== 7:
            answer += "L"
            left_position = [-1,int((i - 0.1)/3)]
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            right_position = [1,int((i - 0.1)/3)]
        else:
            if i == 0:
                middle_position = [0,3]
            else:
                middle_position = [0,int(i/3)]
            
            if abs(left_position[1] - middle_position[1]) + abs(left_position[0] - middle_position[0]) < abs(right_position[1] - middle_position[1]) + abs(right_position[0] - middle_position[0]):
                left_position = middle_position
                answer += "L"
            elif abs(left_position[1] - middle_position[1]) + abs(left_position[0] - middle_position[0]) > abs(right_position[1] - middle_position[1]) + abs(right_position[0] - middle_position[0]):
                answer += "R"
                right_position = middle_position
                
            else:
                if hand == "right":
                    answer += "R"
                    right_position = middle_position
                else:
                    answer += "L"
                    left_position = middle_position
    
    
    return answer

from itertools import permutations

def solution(expression):
    answer = 0
    
    operator = ["*","+","-"]
    
    array = list(permutations(operator,3))
    
    original_word_list = []
    original_oper_list = []
    word = ""
    for i in range(len(expression)):
        
        if expression[i].isdigit():
            word += expression[i]
        else:
            original_oper_list.append(expression[i])
            original_word_list.append(int(word))
            word = ""
    original_word_list.append(int(word))
    
    # 각각의 숫자 리스트와 부호 리스트 채워넣음. 
    
    
    
    max_value = 0
    
    #총 우선순위화로 정리된 튜플 6개 생성
    for i in range(len(array)):
        
        oper_list = original_oper_list[:]
        word_list = original_word_list[:]
        number = 0
        for j in range(len(array[i])):
            while array[i][j] in oper_list:
                index = oper_list.index(array[i][j])
                if array[i][j] == "*":
                    number = word_list[index] * word_list[index + 1]
                elif array[i][j] == "+":
                    number = word_list[index] + word_list[index + 1]
                else:
                    number = word_list[index] - word_list[index + 1]
                oper_list.remove(array[i][j])
                del word_list[index:index+2]
                word_list.insert(index,number)
                
        
        number = abs(number)
        max_value = max(max_value,number)
        
            
            
            
        answer = max_value
            
    
    return answer

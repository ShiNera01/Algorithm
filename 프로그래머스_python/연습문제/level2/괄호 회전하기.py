def correct(word):
    stack = []
    for i in range(len(word)):
        if word[i] in ("[","(","{"):
            stack.append(word[i])
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == "[" and word[i] == "]":
                stack.pop()
            elif stack[-1] == "(" and word[i] == ")":
                stack.pop()
            elif stack[-1] == "{" and word[i] == "}":
                stack.pop()
            else:
                return False
            
    if len(stack) != 0:
        return False
    return True
        
def solution(s):
    answer = 0
    
    test_word = ""
    for i in range(len(s)):
        test_word = s[i:] + s[:i]
        
        if correct(test_word) == True:
            answer += 1
            
        else:
            
            continue
    
    return answer

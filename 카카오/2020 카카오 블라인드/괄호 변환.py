def correct_word(p):
    array = []
    count = 0
    
    for i in p:
        if len(array) == 0 and i == "(":
            array.append(i)
        elif len(array) == 0:
            break
        elif i == ")":
            array.pop()
            count += 1
        elif i == "(":
            array.append(i)
        
        
        if count == len(p)//2:
            return True
        
    return False

def step_1(p):
    
    if len(p) == 0:
        return True
    return False
    
def step_2(p):
    
    left,right = 0,0
    
    u = ""
    v = ""
    
    for i in range(len(p)):
        
        if p[i] == "(":
            left += 1
        elif p[i] == ")":
            right += 1
        
        if left == right and i == len(p) - 1:
            u = p[:i+1]

        elif left == right:
            u = p[:i+1]
            v = p[i+1:]
            break
    
    return u,v

def step_3(u,v):
    
    if correct_word(u) == True:
        if step_1(v) == True:
            return u
        else:
            v_1 = ""
            v_2 = ""
            v_1,v_2 = step_2(v)
        
        return u + step_3(v_1,v_2)
        
    #step4 실행
    else:
        return step_4(u,v)
        
        
    
        
def step_4(u,v):
    
    new_word = ""
    new_word += "("
    new_u = ""
    if step_1(v) == True:
        pass
    else:
        v_1 = ""
        v_2 = ""
        v_1,v_2 = step_2(v)
        
        
        new_word += step_3(v_1,v_2)
        
    
    new_word += ")"
    
    
    if len(u) == 2:
        pass
    else:    
        u = u[1:-1]
        
        for i in range(len(u)):
            if u[i] == ")":
                new_u += "("
            else:
                new_u += ")"
                
    new_word += new_u
    
    
    return new_word
        
    
    
        
    
    
def solution(p):
    answer = ''
    
    if correct_word(p) == True:
        return p
    
    #step 1
    if step_1(p) == True:
        return p
    
    #step 2
    u = ""
    v = ""
    u,v = step_2(p)        
    
    #step 3
    if correct_word(u) == True:
        answer = step_3(u,v)
        
    else:
        
        answer = step_4(u,v)
    


        
    
    return answer

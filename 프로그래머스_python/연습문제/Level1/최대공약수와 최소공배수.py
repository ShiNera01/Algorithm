import math



def solution(n, m):
    answer = []
    
    answer.append(math.gcd(n,m))
    answer.append(math.gcd(n,m) * n//math.gcd(n,m) * m//math.gcd(n,m))
    
    
    return answer

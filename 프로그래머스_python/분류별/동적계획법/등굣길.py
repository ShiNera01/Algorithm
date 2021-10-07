def solution(m, n, puddles):
    answer = 0
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in puddles:
        dp[i[1]][i[0]] = -1
    
    def direct(i,j):
        
        if dp[i][j] == -1:
            return 0
    
        elif dp[i][j] != 0:
            return dp[i][j]
        
        if i == 1 and j == 1:
            dp[i][j] = 1
        
        elif i == 1:
            dp[i][j] = direct(i,j-1)
        
        elif j == 1:
            dp[i][j] = direct(i-1,j)
            
        else:
            dp[i][j] = direct(i-1,j) + direct(i,j-1)
            
        return dp[i][j]
    
    answer = direct(n,m)
    answer = answer % 1000000007
    return answer

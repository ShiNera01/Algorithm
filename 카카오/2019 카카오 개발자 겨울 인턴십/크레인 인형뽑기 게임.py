def solution(board, moves):
    answer = 0
    result = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] == 0:
                continue
            else:
                if len(result) == 0:
                    result.append(board[j][i - 1])
                    board[j][i - 1] = 0
                    break
                
                elif result[-1] == board[j][i - 1]:
                    result.pop()
                    board[j][i - 1] = 0
                    answer += 2
                    break
                
                else:
                    result.append(board[j][i - 1])
                    board[j][i - 1] = 0
                    break
    return answer

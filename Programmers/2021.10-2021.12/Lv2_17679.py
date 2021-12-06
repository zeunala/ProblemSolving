'''
프렌즈4블록

- 블록을 지우는 함수를 만들고 지워지는 블록이 없을 때까지 반복한다.
이 때 지워지는 블록이 겹칠 수 있으므로 각 단계마다 블록을 한 번에 지워야 한다.
여기서는 지워지는 블록을 X로 표시하였다.
* Fail/1st/00:21:44
'''
from copy import deepcopy

def solution(m, n, board):
    answer = 0
    prevAnswer = -1
    board = [list(board[i]) for i in range(m)]
    
    while answer != prevAnswer:
        prevAnswer = answer
        newBoard = deepcopy(board)
        
        # 지워지는 대상 찾음
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 'X' and board[i][j] == board[i][j+1] and board[i][j+1] == board[i+1][j] and board[i+1][j] == board[i+1][j+1]:
                    newBoard[i][j] = 'X'
                    newBoard[i][j+1] = 'X'
                    newBoard[i+1][j] = 'X'
                    newBoard[i+1][j+1] = 'X'
        
        # 지워지는 블록을 한 번에 지움
        for i in range(m):
            for j in range(n):
                if board[i][j] != 'X' and newBoard[i][j] == 'X':
                    board[i][j] = 'X'
                    answer += 1
                    
        # 빈 공간을 채움
        for j in range(n):
            for i in range(m - 1):
                if board[i][j] != 'X' and board[i+1][j] == 'X':
                    board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                    
    return answer
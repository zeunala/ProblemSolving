'''
크레인 인형뽑기 게임

- 문제 그대로 구현하면 되는 문제로 보인다.
게임 화면을 열 단위로 나눠 스택으로 보아서 계산해보자.
* Pass/1st/00:13:20
'''

def solution(board, moves):
    answer = 0
    
    # field[a]는 a열에 대해서 밑에서부터 인형 배열의 스택(배열)이 된다.
    field = [[] for _ in range(len(board[0]))]
    
    for i in range(len(board) - 1, -1, -1): # board의 뒤에서부터 본다.
        for j in range(len(board[i])):
            if board[i][j] != 0:
                field[j].append(board[i][j])
    
    box = [] # 바구니에 있는 인형들
    for e in moves:
        if field[e - 1]:
            popElement = field[e - 1].pop() # moves에 있는 열에서 인형을 뽑음
            box.append(popElement)
    
    isChanged = True # 연쇄적으로 바구니에서 터질 것을 대비해 안터질때까지 반복문을 돌림
    while isChanged:
        isChanged = False
        for i in range(len(box) - 1):
            if box[i] == box[i + 1]:
                box.pop(i)
                box.pop(i)
                isChanged = True
                answer += 2
                break
        
    return answer
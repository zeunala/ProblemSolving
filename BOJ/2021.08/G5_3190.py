'''
뱀

입력
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며.
게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.
'''

'''
- 구현 유형의 문제로 보인다. 조건에 맞춰서 차근차근 구현해 나가면 될 것이다.
* Pass/1st/00:44:22
'''
from queue import deque

N = int(input()) # 보드 크기
K = int(input()) # 사과의 개수
board = [[0 for _ in range(N)] for _ in range(N)] # 보드판. 0은 빈곳. 1은 뱀, 6은 사과를 의미한다.
command = {} # 변환 명령. 몇 초후에 해당하는 부분이 key, 왼쪽/오른쪽에 해당하는 부분이 value
for i in range(K):
    (r, c) = map(int, input().split())
    board[r-1][c-1] = 6 # 코드에서는 0행 0열을 기준으로 하기에 보정
L = int(input())
for i in range(L):
    (a, b) = input().split()
    command[int(a)] = b

time = 0 # 게임 시작하고 몇 초가 흘렀는지
snakeDirection = "R" # 뱀의 진행방향(U, D, L, R)
snakeFrontPositionR = 0 # 뱀의 맨 앞(충돌 체크 위함) 위치의 row
snakeFrontPositionC = 0
snakePosition = deque() # 뱀이 위치하는 곳
snakePosition.append((0, 0)) # 처음 위치를 넣어줌
board[0][0] = 1 # 뱀의 처음 위치

while True:
    time += 1
    if snakeDirection == "U":
        snakeFrontPositionR -= 1
    elif snakeDirection == "D":
        snakeFrontPositionR += 1
    elif snakeDirection == "L":
        snakeFrontPositionC -= 1
    elif snakeDirection == "R":
        snakeFrontPositionC += 1
    
    if snakeFrontPositionR < 0 or snakeFrontPositionR >= N or snakeFrontPositionC < 0 or snakeFrontPositionC >= N: # 보드를 벗어나는 경우 게임 끝
        break
    if board[snakeFrontPositionR][snakeFrontPositionC] == 1: # 뱀과 부딪히는 경우도 게임 끝
        break
    
    if board[snakeFrontPositionR][snakeFrontPositionC] != 6: # 사과를 먹는 경우가 아니라면 뒤를 하나 빼줘야 한다.
        (r, c) = snakePosition.popleft()
        board[r][c] = 0

    snakePosition.append((snakeFrontPositionR, snakeFrontPositionC)) # 현재 위치 추가
    board[snakeFrontPositionR][snakeFrontPositionC] = 1

    if time in command: # 방향 바꾸는 명령이 있는 경우 처리
        if snakeDirection == "U" and command[time] == "L": # 현재 뱀이 위로 가고 있는데 왼쪽으로 가라고 명령하는 경우와 대응
            snakeDirection = "L"
        elif snakeDirection == "U" and command[time] == "D":
            snakeDirection = "R"

        elif snakeDirection == "D" and command[time] == "L":
            snakeDirection = "R"
        elif snakeDirection == "D" and command[time] == "D":
            snakeDirection = "L"

        elif snakeDirection == "L" and command[time] == "L":
            snakeDirection = "D"
        elif snakeDirection == "L" and command[time] == "D":
            snakeDirection = "U"

        elif snakeDirection == "R" and command[time] == "L":
            snakeDirection = "U"
        elif snakeDirection == "R" and command[time] == "D":
            snakeDirection = "D"

print(time)

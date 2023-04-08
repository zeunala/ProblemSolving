'''
새로운 게임 2

입력
첫째 줄에 체스판의 크기 N, 말의 개수 K가 주어진다. 둘째 줄부터 N개의 줄에 체스판의 정보가 주어진다.
체스판의 정보는 정수로 이루어져 있고, 각 정수는 칸의 색을 의미한다. 0은 흰색, 1은 빨간색, 2는 파란색이다.
다음 K개의 줄에 말의 정보가 1번 말부터 순서대로 주어진다.
말의 정보는 세 개의 정수로 이루어져 있고, 순서대로 행, 열의 번호, 이동 방향이다.
행과 열의 번호는 1부터 시작하고, 이동 방향은 4보다 작거나 같은 자연수이고 1부터 순서대로 →, ←, ↑, ↓의 의미를 갖는다.
같은 칸에 말이 두 개 이상 있는 경우는 입력으로 주어지지 않는다.

출력
게임이 종료되는 턴의 번호를 출력한다.
그 값이 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력한다.
'''

'''
- N, K의 범위가 매우 작으므로 효율성을 고려하지 않고 문제의 요구사항을 그대로 직접 구현한다.
말이 4개 이상 쌓이는 순간 턴의 번호를 출력하는데 턴 중간에만 4개 이상 쌓일 수 있음에 유의한다.
* Pass/1st/00:49:07
- 체스판에서의 좌표와 배열에서의 좌표의 차이를 잊고 오른쪽을 (1, 0)과 같이 한 바람에 시간을 많이 소비하였다. 이에 주의해야 할 것으로 보인다.
'''
# 플레이어의 위치를 찾아 (i, j)의 형태로 반환한다.
def findPlayer(mapPlayer, playerIdx):
    for i in range(len(mapPlayer)):
        for j in range(len(mapPlayer[i])):
            if playerIdx in mapPlayer[i][j]:
                return (i, j)
    
N, K = map(int, input().split()) # 체스판의 크기 N, 말의 개수 K
mapArr = [] # 0(흰색), 1(빨간색), 2(파란색)로 이루어진 체스판의 정보. 편의상 1행 1열부터 시작하고 판 주변을 파란색으로 감싼다.
mapPlayer = [[[] for _ in range(N + 2)] for _ in range(N + 2)] # mapArr[i][j]에 위치하는 말들의 배열
directByPlayer = [(0, 0)] * (K + 2) # directByPlayer[i]는 i번 말(i>=1)의 방향, ex. (0, 1)은 아래, (-1, 0)은 왼쪽

mapArr.append([2] * (N + 2))
for i in range(N):
    mapArr.append([2] + list(map(int, input().split())) + [2])
mapArr.append([2] * (N + 2))

for i in range(1, K + 1):
    x, y, d = map(int, input().split())
    mapPlayer[x][y].append(i) # (x, y)에 i번말 추가
    # 방향 설정
    if d == 1:
        directByPlayer[i] = (0, 1)
    elif d == 2:
        directByPlayer[i] = (0, -1)
    elif d == 3:
        directByPlayer[i] = (-1, 0)
    elif d == 4:
        directByPlayer[i] = (1, 0)
    
gameOver = False # 말이 4개 이상 쌓이는 순간 종료
for turn in range(1, 1002):
    for player in range(1, K + 1):
        (posX, posY) = findPlayer(mapPlayer, player)
        nextPosX, nextPosY = posX + directByPlayer[player][0], posY + directByPlayer[player][1] # 다음 위치
        
        if mapArr[nextPosX][nextPosY] == 2: # 파란색
            directByPlayer[player] = (directByPlayer[player][0] * (-1), directByPlayer[player][1] * (-1)) # 방향 변경
            nextPosX, nextPosY = posX + directByPlayer[player][0], posY + directByPlayer[player][1] # 다음 위치 갱신
            
            # 위치 바꿨는데도 파란색이면 그 플레이어는 움직이지 않고 다음 플레이어 이동
            if mapArr[nextPosX][nextPosY] == 2:
                continue
        
        if mapArr[nextPosX][nextPosY] == 0: # 흰색
            moveTarget = mapPlayer[posX][posY][mapPlayer[posX][posY].index(player):] # 해당 말 위에 있는 것까지 한 번에 끌어옴
            mapPlayer[posX][posY] = mapPlayer[posX][posY][:mapPlayer[posX][posY].index(player)]
            mapPlayer[nextPosX][nextPosY].extend(moveTarget)
            
            if len(mapPlayer[nextPosX][nextPosY]) >= 4:
                gameOver = True
                break
        elif mapArr[nextPosX][nextPosY] == 1: # 빨간색
            moveTarget = list(reversed(mapPlayer[posX][posY][mapPlayer[posX][posY].index(player):]))
            mapPlayer[posX][posY] = mapPlayer[posX][posY][:mapPlayer[posX][posY].index(player)]
            mapPlayer[nextPosX][nextPosY].extend(moveTarget)
            
            if len(mapPlayer[nextPosX][nextPosY]) >= 4:
                gameOver = True
                break
    
    if gameOver:
        break

if turn > 1000:
    print(-1)
else:
    print(turn)
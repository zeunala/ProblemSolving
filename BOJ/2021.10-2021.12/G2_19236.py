'''
청소년 상어

입력
첫째 줄부터 4개의 줄에 각 칸의 들어있는 물고기의 정보가 1번 행부터 순서대로 주어진다.
물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향을 의미한다.
방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.

출력
상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 출력한다.
'''

'''
- 필드가 4*4밖에 되지 않으므로 문제 그대로 구현하면 되는 것으로 보인다.
* Fail/1st/02:46:24
- 상어가 이동할 곳을 결정하고 물고기가 움직이게 했는데, 순서가 바뀌어야 상어가 올바른 물고기 지역으로 이동할 수 있다.
* Pass/2nd/02:53:39
'''
from copy import deepcopy

def moveByDirection(pos, direction): # direction값은 문제 입력으로 제시한 1~8값으로, 입력받은 위치에 대하여 이동시 다음 지점을 반환한다.
    (x, y) = pos
    if direction == 1: # ↑
        return (x-1, y)
    elif direction == 2: # ↖
        return (x-1, y-1)
    elif direction == 3: # ←
        return (x, y-1)
    elif direction == 4: # ↙
        return (x+1, y-1)
    elif direction == 5: # ↓
        return (x+1, y)
    elif direction == 6: # ↘
        return (x+1, y+1)
    elif direction == 7: # →
        return (x, y+1)
    elif direction == 8: # ↗
        return (x-1, y+1)

def fishMove(field, fishPosArr):
    resultField = deepcopy(field)

    for i in range(1, 17):
        if fishPosArr[i] == None:
            continue
        
        (posX, posY) = fishPosArr[i]
        for j in range(8): # 최대 8번 시도
            nowDirection = (resultField[fishPosArr[i][0]][fishPosArr[i][1]][1] - 1 + j) % 8 + 1
            
            (posX, posY) = moveByDirection(fishPosArr[i], nowDirection)
            if resultField[posX][posY][0] < 0: # 벽이 있거나 상어가 있음
                continue
            elif resultField[posX][posY][0] == 0: # 빈 곳일 경우
                resultField[fishPosArr[i][0]][fishPosArr[i][1]][0] = 0
                resultField[posX][posY] = [i, nowDirection]
                fishPosArr[i] = (posX, posY)
                break
            elif resultField[posX][posY][0] > 0: # 다른 물고기가 있을 경우
                newFishNum = resultField[posX][posY][0]
                resultField[posX][posY], resultField[fishPosArr[i][0]][fishPosArr[i][1]] = resultField[fishPosArr[i][0]][fishPosArr[i][1]], resultField[posX][posY]
                resultField[posX][posY][1] = nowDirection
                fishPosArr[i], fishPosArr[newFishNum] = fishPosArr[newFishNum], fishPosArr[i]
                break
            
    return resultField

def sharkMove(field, sharkPos, currentScore, fishPosArr): # 상어 이동 후 점수 최댓값 리턴
    canMovePos = [] # 상어가 이동가능한 곳
    nextPos = sharkPos
    
    field = fishMove(field, fishPosArr) # 물고기 이동
    
    while True:
        nextPos = moveByDirection(nextPos, field[sharkPos[0]][sharkPos[1]][1])
        if field[nextPos[0]][nextPos[1]][0] == -1: # 벽이라면 더 이상 이동 불가
            break
        if field[nextPos[0]][nextPos[1]][0] > 0: # 물고기가 있는 곳이면 canMovePos에 추가
            canMovePos.append(nextPos)
            
    if len(canMovePos) == 0: # 상어가 더 이상 진행 불가한 경우 지금까지의 점수 리턴
        return currentScore

    maxScore = currentScore
    for e in canMovePos:
        tempFishPosArr = fishPosArr[:]
        nextField = deepcopy(field)
        nextField[sharkPos[0]][sharkPos[1]][0] = 0 # 상어가 있던 자리는 비워짐
        
        getScore = nextField[e[0]][e[1]][0]
        tempFishPosArr[nextField[e[0]][e[1]][0]] = None # 상어 등장
        nextField[e[0]][e[1]][0] = -2
        
        nextScore = sharkMove(nextField, e, currentScore + getScore, tempFishPosArr)
        
        if maxScore < nextScore:
            maxScore = nextScore
    
    return maxScore
    
    

# (필드정보, 방향)의 원소들로 구성. 0은 빈 곳, -1은 벽, 상어는 -2로 표시해서 물고기가 이동할 때 0이상인 곳으로만 이동하도록 한다.
field = [[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]],
         [[-1, -1], [0, -1], [0, -1], [0, -1], [0, -1], [-1, -1]],
         [[-1, -1], [0, -1], [0, -1], [0, -1], [0, -1], [-1, -1]],
         [[-1, -1], [0, -1], [0, -1], [0, -1], [0, -1], [-1, -1]],
         [[-1, -1], [0, -1], [0, -1], [0, -1], [0, -1], [-1, -1]],
         [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]]

fishPosArr = [(0, 0) for _ in range(17)] # fishPosArr[i]는 i(1~16)번 물고기의 위치. 이미 먹혔으면 None이 됨
fishPosArr[0] = None

for i in range(1, 5):
    inputArr = list(map(int, input().split()))
    field[i][1] = [inputArr[0], inputArr[1]]
    field[i][2] = [inputArr[2], inputArr[3]]
    field[i][3] = [inputArr[4], inputArr[5]]
    field[i][4] = [inputArr[6], inputArr[7]]

for i in range(1, 5):
    for j in range(1, 5):
        fishPosArr[field[i][j][0]] = (i, j)    

currentScore = field[1][1][0] # 상어가 먹은 물고기 번호 합 (처음엔 첫칸에 있는 물고기 번호)

fishPosArr[field[1][1][0]] = None # 상어 등장
field[1][1][0] = -2

print(sharkMove(field, (1, 1), currentScore, fishPosArr))

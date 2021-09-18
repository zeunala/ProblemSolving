'''
캐슬 디펜스

입력
첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다.
둘째 줄부터 N개의 줄에는 격자판의 상태가 주어진다.
0은 빈 칸, 1은 적이 있는 칸이다.

출력
첫째 줄에 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력한다.
'''

'''
- 궁수를 놓을 수 있는 모든 경우의 수에 대해 연산해보자.
* Pass/1st/01:01:39
'''
from copy import deepcopy
from itertools import combinations
from queue import deque

def findTarget(arr, N, M, D, pos): # pos열에 있는 궁수가 쏘게 될 적의 좌표를 리턴. 없으면 (-1, -1)을 리턴한다.
    nextFindArr = deque([(N-1, pos)]) # 거리 1인 건 마지막행 같은 열이다.
    visited = [[False for _ in range(M)] for _ in range(N)]
    while(nextFindArr):
        nextFind = nextFindArr.popleft()
        if visited[nextFind[0]][nextFind[1]]:
            continue
        visited[nextFind[0]][nextFind[1]] = True

        if (abs(N-nextFind[0])+abs(pos-nextFind[1]))>D: # 만약 도중 사정거리를 초과했을 경우 못찾은 것으로 보고 break(BFS탐색이므로)
            break
        if arr[nextFind[0]][nextFind[1]] == 1: # 적을 만났으면 바로 그 위치 리턴
            return (nextFind[0], nextFind[1])
        else: # 아닐 경우 주변 칸들을 큐에 넣되 왼쪽것을 우선순위로 먼저 넣는다.
            if nextFind[1]-1 >= 0 and visited[nextFind[0]][nextFind[1]-1] == False:
                nextFindArr.append((nextFind[0], nextFind[1]-1)) # 왼쪽
            if nextFind[0]-1 >= 0 and visited[nextFind[0]-1][nextFind[1]] == False:
                nextFindArr.append((nextFind[0]-1, nextFind[1])) # 위
            if nextFind[1]+1 < M and visited[nextFind[0]][nextFind[1]+1] == False:
                nextFindArr.append((nextFind[0], nextFind[1]+1)) # 오른쪽

    return (-1, -1) # 못찾음

def findCase(arr, N, M, D, enemyNum, d1, d2, d3): # 궁수가 d1열, d2열, d3열에 놓였을 경우 제거가능한 적의 수 (0열부터 시작)
    killEnemyNum = 0 # 제거한 적의 수
    tempArr = deque(deepcopy(arr))


    while enemyNum > 0:
        target1 = findTarget(tempArr, N, M, D, d1)
        target2 = findTarget(tempArr, N, M, D, d2)
        target3 = findTarget(tempArr, N, M, D, d3)

        if target1[0] != -1 and tempArr[target1[0]][target1[1]] == 1: # 궁수가 제대로 찾았고 그 위치에 적이 있으면 쏜다
            tempArr[target1[0]][target1[1]] = 0
            killEnemyNum += 1
            enemyNum -= 1
        
        if target2[0] != -1 and tempArr[target2[0]][target2[1]] == 1: # 궁수가 제대로 찾았고 그 위치에 적이 있으면 쏜다
            tempArr[target2[0]][target2[1]] = 0
            killEnemyNum += 1
            enemyNum -= 1

        if target3[0] != -1 and tempArr[target3[0]][target3[1]] == 1: # 궁수가 제대로 찾았고 그 위치에 적이 있으면 쏜다
            tempArr[target3[0]][target3[1]] = 0
            killEnemyNum += 1
            enemyNum -= 1

        tempArr.appendleft([0 for _ in range(M)]) # 맨 앞에 0들 추가하고 맨 끝을 pop하면 한 칸씩 앞으로 간 셈이다.
        remainEnemy = tempArr.pop()

        for i in range(M):
            if remainEnemy[i] == 1: # 맨 끝에 도달한 적은 제거된다.
                enemyNum -= 1
    
    return killEnemyNum
        
N, M, D = map(int, input().split()) # 각각 행, 열, 궁수의 거리제한
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

enemyNum = 0 # 적의 수
maximumKill = 0 # 문제에서 요구하는 답(최대 제거가능한 적의 수)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            enemyNum += 1

for e in combinations([i for i in range(M)], 3):
    (d1, d2, d3) = e
    killEnemyNum = findCase(arr, N, M, D, enemyNum, d1, d2, d3)
    if killEnemyNum > maximumKill:
        maximumKill = killEnemyNum

print(maximumKill)
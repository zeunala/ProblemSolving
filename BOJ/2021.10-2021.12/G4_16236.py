'''
아기 상어

입력
첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에 공간의 상태가 주어진다.
공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
아기 상어는 공간에 한 마리 있다.

출력
첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.
'''

'''
- 자기 위치를 기준으로 물고기를 BFS탐색을 하되 위쪽/왼쪽/오른쪽/아래쪽 순서대로 탐색한다.
BFS탐색을 하였으면 그 결과에 대해 시간경과/상어성장/공간변화가 일어나고, BFS탐색을 실패할 경우 종료하게 된다.
* Fail/1st/00:50:50
- 우선 방향을 둔 것만으로 우선순위가 구현 될 줄 알았는데, 구현한 방법에선 현재 위치 기준 오른쪽 두칸보다 왼쪽 한칸+아래쪽 한칸이 우선순위가 잡힌다.
일단 같은 거리에 있는 걸 다 구해보고 그 중에서 고르는 식으로 구현해야 할 것으로 보인다.
* Pass/2nd/01:19:00
'''
from queue import deque

def bfs(field, N, playerPos, playerLevel): # bfs로 다음 물고기를 찾고 그 때까지 걸리는 시간을 리턴. 못찾으면 -1리턴 (이 때 field와 playerPos변화)
    visited = [[False for _ in range(N)] for _ in range(N)]
    bfsQueue = deque() # 위치와 비용이 저장된다.
    bfsQueue.append((playerPos, 0))
    
    possiblePos = [] # 잡아 먹을 수 있는 모든 물고기들의 위치들
    possibleCost = 999
    
    while bfsQueue:
        (currentPos, currentCost) = bfsQueue.popleft()
        
        if visited[currentPos[0]][currentPos[1]]:
            continue
        visited[currentPos[0]][currentPos[1]] = True
        
        if possibleCost < currentCost: # 현재 탐색 거리보다 더 짧은 경로가 존재하므로 더 탐색할 필요 없음
            break
        
        # 자기보다 작은 물고기를 만난 경우 (deque에 넣을 때 검사는 하지만 자신과 크기가 같은 물고기를 만날 수도 있기에 다시 검사 필요)
        if field[currentPos[0]][currentPos[1]] > 0 and field[currentPos[0]][currentPos[1]] < playerLevel:
            possiblePos.append(currentPos)
            possibleCost = currentCost
        
        # 다음 칸을 탐색하는 단계, 위쪽/왼쪽/오른쪽/아래쪽 순서대로 탐색한다
        if currentPos[0] - 1 >= 0 and visited[currentPos[0] - 1][currentPos[1]] == False and field[currentPos[0] - 1][currentPos[1]] <= playerLevel:
            bfsQueue.append(([currentPos[0] - 1, currentPos[1]], currentCost + 1))
        if currentPos[1] - 1 >= 0 and visited[currentPos[0]][currentPos[1] - 1] == False and field[currentPos[0]][currentPos[1] - 1] <= playerLevel:
            bfsQueue.append(([currentPos[0], currentPos[1] - 1], currentCost + 1))
        if currentPos[1] + 1 < N and visited[currentPos[0]][currentPos[1] + 1] == False and field[currentPos[0]][currentPos[1] + 1] <= playerLevel:
            bfsQueue.append(([currentPos[0], currentPos[1] + 1], currentCost + 1))
        if currentPos[0] + 1 < N and visited[currentPos[0] + 1][currentPos[1]] == False and field[currentPos[0] + 1][currentPos[1]] <= playerLevel:
            bfsQueue.append(([currentPos[0] + 1, currentPos[1]], currentCost + 1))
            
    if possiblePos: # 경로를 찾은 경우
        possiblePos.sort() # 행이 작은 것 우선, 행이 같다면 열이 작은 것 우선으로 정렬
        field[possiblePos[0][0]][possiblePos[0][1]] = 0 # 가장 우선순위가 높은 곳으로 이동하여 먹음
        playerPos[0] = possiblePos[0][0]
        playerPos[1] = possiblePos[0][1]
        return possibleCost
    else:
        return -1

N = int(input())
field = []
for i in range(N):
    field.append(list(map(int, input().split())))
    
playerPos = None # 아기상어 위치
for i in range(N):
    for j in range(N):
        if field[i][j] == 9: # 9라고 적혀있는 곳을 지우고 playerPos로 위치를 별도 관리한다.
            field[i][j] = 0
            playerPos = [i, j]

playerLevel = 2 # 상어 크기           
playerExp = 0 # playerLevel만큼의 물고기를 먹으면 playerLevel이 1 오른다.
totalTime = 0

while True:
    timeSpend = bfs(field, N, playerPos, playerLevel)
    if timeSpend != -1:
        totalTime += timeSpend
        playerExp += 1
        if playerExp >= playerLevel:
            playerLevel += 1
            playerExp = 0
    else:
        break

print(totalTime)
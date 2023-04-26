'''
두 동전

입력
첫째 줄에 보드의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 20)
둘째 줄부터 N개의 줄에는 보드의 상태가 주어진다.
o: 동전
.: 빈 칸
#: 벽
동전의 개수는 항상 2개이다.

출력
첫째 줄에 두 동전 중 하나만 보드에서 떨어뜨리기 위해 눌러야 하는 버튼의 최소 횟수를 출력한다.
만약, 두 동전을 떨어뜨릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면, -1을 출력한다.
'''

'''
- 버튼 누르는 횟수를 10번까지만 탐색하면 되므로 모든 경우의 수를 탐색하도록 한다.
* Pass/1st/00:27:07(use PyPy3)
'''
from itertools import product

# 주어진 행동 U/D/L/R들을 순서대로 수행했을 때 두 동전 중 하나만 보드에서 떨어지는지 여부 리턴
def isSuccess(mapArr, actions, N, M, coinPos1, coinPos2):
    di = {"U": -1, "D": 1, "L": 0, "R": 0}
    dj = {"U": 0, "D": 0, "L": -1, "R": 1}
    
    dropCount = 0 # 몇 개의 동전이 떨어졌는지
    for action in actions:
        coinPos1 = (coinPos1[0] + di[action], coinPos1[1] + dj[action])
        coinPos2 = (coinPos2[0] + di[action], coinPos2[1] + dj[action])
        
        if coinPos1[0] < 0 or coinPos1[0] >= N or coinPos1[1] < 0 or coinPos1[1] >= M: # 동전이 떨어질 경우
            dropCount += 1
        elif mapArr[coinPos1[0]][coinPos1[1]] == "#": # 이동하려는 곳에 벽이 있는 경우 이동 취소
            coinPos1 = (coinPos1[0] - di[action], coinPos1[1] - dj[action])
                
        if coinPos2[0] < 0 or coinPos2[0] >= N or coinPos2[1] < 0 or coinPos2[1] >= M: # 동전이 떨어질 경우
            dropCount += 1
        elif mapArr[coinPos2[0]][coinPos2[1]] == "#": # 이동하려는 곳에 벽이 있는 경우 이동 취소
            coinPos2 = (coinPos2[0] - di[action], coinPos2[1] - dj[action])
                
        if dropCount == 1: # 두 동전 중 하나만 보드에 떨어지는 시점이 오면 성공
            return True
        if dropCount == 2: # 두 동전이 동시에 떨어지면 실패
            return False
        
    return False # 주어진 행동 모두 수행했는데도 조건 충족 못하면 실패

N, M = map(int, input().split())
mapArr = []

coinPos1 = None # 첫 번째 코인의 위치
coinPos2 = None # 두 번째 코인의 위치

for i in range(N):
    mapArr.append(list(input()))
    
# 보드에서 동전(o)을 빈 칸으로 바꾸고 위치만 기록해둔다.
for i in range(N):
    for j in range(M):
        if mapArr[i][j] == "o":
            mapArr[i][j] = "."
            
            if coinPos1 == None:
                coinPos1 = (i, j)
            else:
                coinPos2 = (i, j)
    
answer = -1 # 눌러야 하는 버튼의 최소 횟수, 없으면 -1
for actionCount in range(1, 11):
    if answer != -1:
        break
    
    for actions in product(["U", "D", "L", "R"], repeat = actionCount):
        if isSuccess(mapArr, actions, N, M, coinPos1, coinPos2):
            answer = actionCount
            break
        
print(answer)
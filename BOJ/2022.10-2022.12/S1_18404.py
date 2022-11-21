'''
현명한 나이트

입력
첫째 줄에 N과 M이 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ N ≤ 500, 1 ≤ M ≤ 1,000)
둘째 줄에 나이트의 위치 (X, Y)를 의미하는 X와 Y가 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ X, Y ≤ N)
셋째 줄부터 M개의 줄에 걸쳐 각 상대편 말의 위치 (A, B)를 의미하는 A와 B가 공백을 기준으로 구분되어 자연수로 주어진다.
(1 ≤ A, B ≤ N)
단, 입력으로 주어지는 모든 말들의 위치는 중복되지 않으며, 나이트가 도달할 수 있는 위치로만 주어진다.

출력
첫째 줄에 각 상대편 말을 잡기 위한 최소 이동 수를 공백을 기준으로 구분하여 출력한다.
단, 출력할 때는 입력 시에 상대편 말 정보가 주어졌던 순서에 맞게 차례대로 출력한다.
'''

'''
- BFS를 이용하여 출발지에서 이동할 수 있는 모든 좌표까지의 거리를 구한다.
* Pass/1st/00:12:18
'''
import sys
from collections import deque

INF = 10**10

N, M = map(int, sys.stdin.readline().rstrip().split())
posX, posY = map(int, sys.stdin.readline().rstrip().split())
minStepArr = [[INF for _ in range(N)] for _ in range(N)]
targetArr = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    targetArr.append((a - 1, b - 1))

tempQueue = deque() # (x좌표, y좌표, 해당좌표로의 걸음수)의 큐
tempQueue.append((posX - 1, posY - 1, 0))
while tempQueue:
    x, y, step = tempQueue.popleft()
    
    if minStepArr[x][y] <= step:
        continue
    
    minStepArr[x][y] = step
    
    for (dx, dy) in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
        newX = x + dx
        newY = y + dy
        if newX >= 0 and newX < N and newY >= 0 and newY < N and minStepArr[newX][newY] > step + 1:
            tempQueue.append((newX, newY, step + 1))
            
for e in targetArr:
    a, b = e
    print(minStepArr[a][b], end = " ")

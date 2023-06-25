'''
토마토

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
단, 2 ≤ M,N ≤ 1,000 이다.
둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.
즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.
하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다.
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''

'''
- BFS로 익은 토마토의 좌표와 그 토마토가 며칠째에 익었는지를 함께 저장하여 탐색한다.
인접한 토마토를 모두 방문했을 때 가장 마지막에 익은 토마토의 날짜를 출력하되, 만약 익지 않은 토마토가 남아있다면 -1을 출력한다.
* Pass/1st/00:10:49
'''
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split()) # M: 가로, N: 세로
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

answer = 0
visitedQueue = deque() # (세로좌표, 가로좌표, 며칠째에 익었는지)를 저장

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            visitedQueue.append((i, j, 0))
            
while visitedQueue:
    i, j, t = visitedQueue.popleft()
    answer = max(answer, t)
    
    for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        newI = i + di
        newJ = j + dj
        
        if newI >= 0 and newI < N and newJ >= 0 and newJ < M and arr[newI][newJ] == 0:
            arr[newI][newJ] = 1 # 방문처리도 겸함
            visitedQueue.append((newI, newJ, t + 1))
            
isAllComplete = True # 모든 토마토가 익었는지 여부
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            isAllComplete = False
            
if isAllComplete:
    print(answer)
else:
    print(-1)
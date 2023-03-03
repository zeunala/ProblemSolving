'''
내 선물을 받아줘

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000, 1 < N×M ≤ 1,000,000)
둘째 줄부터 N개의 줄에는 구사과가 있는 곳의 지도가 주어진다. 
지도에 쓰여 있는대로 이동했을 때, 지도를 벗어나는 경우는 없다.

출력
첫째 줄에 최소 몇 개의 칸에 선물을 놓아야 하는지 출력한다.
'''

'''
- 모든 장소에서 한 방향으로 이동할 수 있음이 보장되므로(지도를 벗어나는 경우가 없다고 하였다),
반드시 이동 경로는 싸이클의 형태가 된다.
전체 지도를 탐색하여 총 몇 개의 묶음이 나오는지만 판단하면 된다.
* Fail/1st/00:13:26
'''
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
mapArr = []
visited = [[False for _ in range(M)] for _ in range(N)]

di = {"N": -1, "E": 0, "W": 0, "S": 1} # ex. di["N"]는 (i, j)에서 N방향 이동시 i의 변화량
dj = {"N": 0, "E": 1, "W": -1, "S": 0}
answer = 0

for i in range(N):
    mapArr.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(M):
        # 방문한 칸이면 패스
        if visited[i][j]:
            continue
        
        # 방문하지 않은 칸이라면 지금부터는 한 덩이를 세는 과정임
        answer += 1
        
        # 방문하지 않은 각 칸이 나올 때까지 계속 이동하며 탐색
        currentI, currentJ = i, j
        while visited[currentI][currentJ] == False:
            visited[currentI][currentJ] = True
            
            currentPos = mapArr[currentI][currentJ] # 현재 위치한 알파벳
            currentI += di[currentPos]
            currentJ += dj[currentPos]
            
print(answer)
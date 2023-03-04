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
- 반드시 싸이클이 된다는 보장이 없다. "(싸이클)<-<-"의 형태도 가능하기 때문이다.
싸이클 안에 선물을 두면 해당 경로 어디든지 접근할 수 있는건 동일하나, 묶음의 개수를 세는 과정에서 주의하도록 한다.
* Pass/2nd/00:25:58
'''
import sys

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
        
        # 현재 탐색하는 곳에서 방문하는 위치들
        currentPath = set()
        
        # 방문하지 않은 각 칸이 나올 때까지 계속 이동하며 탐색
        currentI, currentJ = i, j
        while True:
            if visited[currentI][currentJ]:
                # 현재 탐색하는 곳 내에서 싸이클이 이루어지는 경우 한 묶음이 추가된다.
                # "(싸이클)<-<-" 과 같이 그 전에 이미 탐색한 싸이클을 향하는 경로에 대해서는 한 묶음이 추가되지 않는다.
                if (currentI, currentJ) in currentPath:
                    answer += 1
                break
                
            visited[currentI][currentJ] = True
            currentPath.add((currentI, currentJ))
            
            currentPos = mapArr[currentI][currentJ] # 현재 위치한 알파벳
            currentI += di[currentPos]
            currentJ += dj[currentPos]
            
print(answer)
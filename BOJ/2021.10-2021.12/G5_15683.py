'''
감시

입력
첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 
CCTV의 최대 개수는 8개를 넘지 않는다.

출력
첫째 줄에 사각 지대의 최소 크기를 출력한다
'''

'''
- 사무실의 크기도 작고 CCTV의 개수제한도 적으므로 모든 경우의 수를 하나하나 계산하면 될 것이다.
문제에선 CCTV를 5가지로 나눴지만 좀 더 세분화해보자.
1~15로 나누어서 1은 12시, 2는 3시, 4는 6시, 8은 9시방향을 볼 수 있음을 의미하며 9=1+8로 12시/9시 모두 볼 수 있다고 하자.
* Pass/1st/01:00:48
- 실제 개수와 관계 없이 CCTV 개수를 최대개수인 8개로 잡고 product로 경우의 수를 다 구해놓고 계산했는데 매우 비효율적으로 된 것 같다.
그냥 다른 사람의 풀이처럼 dfs함수 만들어서 최대 개수 채웠을 때 함수호출해 사각지대 수 확인하는 방법이 훨씬 나을 것으로 보인다.
'''
from copy import deepcopy
from itertools import product

def checkArea(room, N, M): # CCTV번호가 세분화되어있고 벽이 -1로 표시되도록 주어졌을 때 감시영역(-2)을 칠하고 사각지대 수를 리턴한다.
    tempRoom = deepcopy(room)
    for i in range(N):
        for j in range(M):
            if tempRoom[i][j] > 0: # CCTV일 때
                if tempRoom[i][j] % 2 == 1: # 12시
                    idx = i - 1
                    while idx >= 0:
                        if tempRoom[idx][j] != -1:
                            if tempRoom[idx][j] == 0:
                                tempRoom[idx][j] = -2
                            idx -= 1
                        else:
                            break
                if (tempRoom[i][j] >> 1 ) % 2 == 1: # 3시
                    idx = j + 1
                    while idx < M:
                        if tempRoom[i][idx] != -1:
                            if tempRoom[i][idx] == 0:
                                tempRoom[i][idx] = -2
                            idx += 1
                        else:
                            break
                if (tempRoom[i][j] >> 2 ) % 2 == 1: # 6시
                    idx = i + 1
                    while idx < N:
                        if tempRoom[idx][j] != -1:
                            if tempRoom[idx][j] == 0:
                                tempRoom[idx][j] = -2
                            idx += 1
                        else:
                            break
                if (tempRoom[i][j] >> 3 ) % 2 == 1: # 9시
                    idx = j - 1
                    while idx >= 0:
                        if tempRoom[i][idx] != -1:
                            if tempRoom[i][idx] == 0:
                                tempRoom[i][idx] = -2
                            idx -= 1
                        else:
                            break

    result = 0
    for i in range(N):
        for j in range(M):
            if tempRoom[i][j] == 0:
                result += 1

    return result

N, M = map(int, input().split())
room = []
# 예를 들어 toDetailNum[2]는 문제의 2번 CCTV가 세분화한 번호 기준으로 몇 번들이 가능한지 나타낸다.
toDetailNum = [[], [1, 2, 4, 8], [5, 10, 5, 10], [3, 6, 9, 12], [7, 11, 13, 14], [15, 15, 15, 15]]
for i in range(N):
    room.append(list(map(int, input().split())))

minCount = 64 # 최소 사각 지대 수
cctvType = [] # cctv가 1~5번 중 몇 번인지
cctvPos = [] # cctv 위치

for i in range(N):
    for j in range(M):
        if room[i][j] == 6: # 벽을 -1로 바꿈
            room[i][j] = -1
        if room[i][j] >= 1 and room[i][j] <= 5:
            cctvType.append(room[i][j])
            cctvPos.append((i, j))

allCase = product([0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3])
for e in allCase:
    for i in range(len(cctvType)):
        room[cctvPos[i][0]][cctvPos[i][1]] = toDetailNum[cctvType[i]][e[i]]
    result = checkArea(room, N, M)
    if minCount > result:
        minCount = result

print(minCount)
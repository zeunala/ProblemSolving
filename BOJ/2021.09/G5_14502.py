'''
연구소

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에 지도의 모양이 주어진다.
0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다.
2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
빈 칸의 개수는 3개 이상이다.

출력
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
'''

'''
- 지도 최대 크기는 64이고, 벽을 놓는 모든 경우의 수는 64C3이하일 것이다. 따라서 모든 경우의 수를 계산해서 안전 영역 크기를 구해보자.
* Pass/1st/00:27:05
'''
from itertools import combinations
from copy import deepcopy

def spreadVirus(arr, virusRow, virusCol, N, M): # 바이러스 위치를 입력받고 DFS방식으로 퍼뜨림
    if virusRow + 1 < N and arr[virusRow+1][virusCol] == 0: # 빈칸에 대해 퍼뜨림
        arr[virusRow+1][virusCol] = 2
        spreadVirus(arr, virusRow+1, virusCol, N, M)
    if virusCol + 1 < M and arr[virusRow][virusCol+1] == 0:
        arr[virusRow][virusCol+1] = 2
        spreadVirus(arr, virusRow, virusCol+1, N, M)
    if virusRow - 1 >= 0 and arr[virusRow-1][virusCol] == 0:
        arr[virusRow-1][virusCol] = 2
        spreadVirus(arr, virusRow-1, virusCol, N, M)
    if virusCol - 1 >= 0 and arr[virusRow][virusCol-1] == 0:
        arr[virusRow][virusCol-1] = 2
        spreadVirus(arr, virusRow, virusCol-1, N, M)

def checkSafetyArea(arr, N, M, virusPos): # 벽이 세워진 필드와 바이러스 위치를 입력받아 바이러스를 퍼뜨린 뒤 안전지대 개수 체크
    for i in range(len(virusPos)):
        spreadVirus(arr, virusPos[i][0], virusPos[i][1], N, M)
    
    safetyArea = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                safetyArea += 1

    return safetyArea


N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

canBlock = [] # 벽을 세울 수 있는 공간에 대한 튜플들 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            canBlock.append((i, j))

virusPos = [] # 바이러스가 위치하는 장소에 대한 튜플들 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virusPos.append((i, j))

maximum = 0
for e in list(combinations(canBlock, 3)): # 모든 경우의 수 생각
    tempArr = deepcopy(arr)
    wall1 = e[0]
    wall2 = e[1]
    wall3 = e[2]
    tempArr[wall1[0]][wall1[1]] = 1
    tempArr[wall2[0]][wall2[1]] = 1
    tempArr[wall3[0]][wall3[1]] = 1
    
    safetyArea = checkSafetyArea(tempArr, N, M, virusPos)
    if maximum < safetyArea:
        maximum = safetyArea
    
print(maximum)
'''
치킨 배달

입력
첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다.
집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다.
치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

출력
첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.
'''

'''
- 치킨 집의 개수가 적기 때문에 모든 치킨집의 경우의 수에 대해 도시의 치킨 거리를 구하고 이들 중 최솟값을 구하면 될 것이다.
* Pass/1st/00:21:14
'''
from itertools import combinations
import sys
from copy import deepcopy

def findMinimumDistance(arr, N, housePos, tempCHousePos): # 주어진 도시상황과 집/치킨집들의 정보에 대한 도시의 치킨 거리를 구한다.
    result = 0

    for e in housePos:
        minDistance = 10**9
        for e2 in tempCHousePos:
            temp = abs(e2[0]-e[0]) + abs(e2[1]-e[1])
            if minDistance > temp:
                minDistance = temp
        result += minDistance

    return result


N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [] # 0, 1, 2로 나타난 도시의 정보
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

housePos = [] # 1로 표시된 집들의 위치정보 (0행 0열부터 시작한다고 가정)
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            housePos.append((i, j))

cHousePos = [] # 2로 표시된 치킨집들의 위치정보 (0행 0열부터 시작한다고 가정)
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            cHousePos.append((i, j))

minimum = 10**9
for e in combinations(cHousePos, M): # 남겨줄 치킨집들의 위치정보들이 e에 담긴다.
    tempArr = deepcopy(arr)
    for e2 in e:
        tempArr[e2[0]][e2[1]] = 0 # 2로 적힌 치킨집을 0으로 두어 폐업시킴

    tempDistance = findMinimumDistance(tempArr, N, housePos, e)
    if minimum > tempDistance:
        minimum = tempDistance

print(minimum)
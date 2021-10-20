'''
게리맨더링

입력
첫째 줄에 구역의 개수 N이 주어진다. 둘째 줄에 구역의 인구가 1번 구역부터 N번 구역까지 순서대로 주어진다. 인구는 공백으로 구분되어져 있다.
셋째 줄부터 N개의 줄에 각 구역과 인접한 구역의 정보가 주어진다.
각 정보의 첫 번째 정수는 그 구역과 인접한 구역의 수이고, 이후 인접한 구역의 번호가 주어진다. 모든 값은 정수로 구분되어져 있다.
구역 A가 구역 B와 인접하면 구역 B도 구역 A와 인접하다. 인접한 구역이 없을 수도 있다.

출력
첫째 줄에 백준시를 두 선거구로 나누었을 때, 두 선거구의 인구 차이의 최솟값을 출력한다. 두 선거구로 나눌 수 없는 경우에는 -1을 출력한다.
'''

'''
- N이 최대 10밖에 되지 않는다. 우선 N을 공집합이 아닌 두 개의 집합으로 분류하는 경우의 수를 모두 나열한다.
그리고 각 경우의 수에 대해 각 집합이 서로 연결되어 있는지 체크해서 선거구가 바르게 나눠진 경우 인구 차이를 계산해보자.
* Pass/1st/00:58:21
'''
from queue import deque

MAXIMUM = 1000000

def findAllCase(connectArr, peopleNum, N, targetN, areaPart): # 1번~N번 구역 중 적절히 나누는 경우를 리턴하여 계산 (areaPart[i]의 True/False로 어디 선거구인지 구분함)
    if targetN > N:
        if findCorrectArea(connectArr, areaPart, N):
            return findPeopleSub(peopleNum, areaPart, N)
        else:
            return MAXIMUM
    
    caseA = findAllCase(connectArr, peopleNum, N, targetN + 1, areaPart+[True])
    caseB = findAllCase(connectArr, peopleNum, N, targetN + 1, areaPart+[False])
    return min(caseA, caseB)

def findCorrectArea(connectArr, areaPart, N): # 선거구가 바르게 나눠졌는지 체크
    areaA = [i for i in range(1, N+1) if areaPart[i] == True]
    areaB = [i for i in range(1, N+1) if areaPart[i] == False]

    if len(areaA) == 0 or len(areaB) == 0:
        return False
    
    visitedA = [False] * (N+1)
    visitedB = [False] * (N+1)
    visitedA[0] = True
    visitedB[0] = True
    for i in range(1, N+1):
        if areaPart[i] == True: # areaA에 속한 것은 B입장에서 이미 visited로 본다.
            visitedB[i] = True
        else:
            visitedA[i] = True

    # A쪽을 BFS로 순회
    tempDeque = deque([])
    tempDeque.append(areaA[0])
    while tempDeque:
        temp = tempDeque.popleft()
        if visitedA[temp]:
            continue

        visitedA[temp] = True
        for e in connectArr[temp]:
            if visitedA[e] == False:
                tempDeque.append(e)

    tempDeque2 = deque([])
    tempDeque2.append(areaB[0])
    while tempDeque2:
        temp2 = tempDeque2.popleft()
        if visitedB[temp2]:
            continue

        visitedB[temp2] = True
        for e in connectArr[temp2]:
            if visitedB[e] == False:
                tempDeque2.append(e)

    # 이렇게 각각 BFS로 탐색했을 때 모두 visited가 찍혀있어야 각각 연결되어 있으므로 조건에 맞다고 할 수 있다.
    for i in range(1, N+1):
        if visitedA[i] == False:
            return False
        if visitedB[i] == False:
            return False
    
    return True

def findPeopleSub(peopleNum, areaPart, N): # 인구수 차이 리턴
    peopleA = 0
    peopleB = 0

    for i in range(1, N+1):
        if areaPart[i]:
            peopleA += peopleNum[i]
        else:
            peopleB += peopleNum[i]

    return abs(peopleA-peopleB)

N = int(input())
peopleNum = [None] + list(map(int, input().split())) # peopleNum[i]는 i번구역(i>=1)의 인구수
connectArr = [[None]] # arr[i]는 i번구역이 연결된 구역들의 번호
for i in range(N):
    tempArr = list(map(int, input().split()))
    connectArr.append(tempArr[1:])

result = findAllCase(connectArr, peopleNum, N, 1, [None])
if result == MAXIMUM:
    print(-1)
else:
    print(result)


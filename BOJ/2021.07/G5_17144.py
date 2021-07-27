'''
미세먼지 안녕!

입력
첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.
둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다.
공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다.
-1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.

출력
첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.
'''

'''
- R, C 범위가 크지 않아 그냥 문제 그대로 구현만 하면 되는 문제로 보인다.
편한 계산을 위해 1행 1열부터 시작한다고 하고 테두리에 벽의 값으로 -2를 두자.
* Pass/1st/00:51:21(use PyPy3)
Python3로는 시간초과가 발생하였으나 삼성역량테스트에 쓰는 pypy3으로는 정답처리되었다.
다른 사람들의 풀이를 찾아보니 접근방법은 맞았지만 최적화가 좀 더 필요한 듯 싶다.
'''
import sys
R, C, T = map(int, input().split()) # 총 R행 C열, T초 후의 미세먼지 양을 계산
arr = []

arr.append([-2 for _ in range(C+2)]) # -2는 벽을 의미
for i in range(R):
    arr.append([-2]+list(map(int, sys.stdin.readline().rstrip().split()))+[-2])
arr.append([-2 for _ in range(C+2)])

cleanerPos = 0 # 공기청정기 위치 확인(공기청정기는 arr[cleanerPos][1]~arr[cleanerPos+1][1]에 위치)
for i in range(R+1):
    if(arr[i][1]==-1):
        cleanerPos = i
        break

for t in range(T): # 총 T회 반복
    # 미세먼지 확산 단계(모든 칸에서 동시에 확산해야함)
    spreadArr = [[0 for _ in range(C+2)] for _ in range(R+2)] # 확산되는 양을 한번에 반영하기 위함
    for i in range(1, R+1):
        for j in range(1, C+1):
            spread = arr[i][j]//5 # 확산되는 양
            if(spread<=0): continue # 확산되는 양이 없거나 arr[i][j]가 -1인 경우 모두 걸러냄

            if(arr[i-1][j]>=0):
                spreadArr[i-1][j]+=spread
                spreadArr[i][j]-=spread

            if(arr[i+1][j]>=0):
                spreadArr[i+1][j]+=spread
                spreadArr[i][j]-=spread

            if(arr[i][j-1]>=0):
                spreadArr[i][j-1]+=spread
                spreadArr[i][j]-=spread

            if(arr[i][j+1]>=0):
                spreadArr[i][j+1]+=spread
                spreadArr[i][j]-=spread

    for i in range(1, R+1):
        for j in range(1, C+1):
            arr[i][j]+=spreadArr[i][j]

    # 공기청정기 윗방향
    temp = arr[cleanerPos].pop(C)
    arr[cleanerPos].insert(2, 0)
    for i in range(cleanerPos-1, 0, -1):
        arr[i][C], temp = temp, arr[i][C]
    arr[1].insert(C, temp)
    temp = arr[1].pop(1)
    for i in range(2, cleanerPos):
        arr[i][1], temp = temp, arr[i][1]

    # 공기청정기 아랫방향
    temp = arr[cleanerPos+1].pop(C)
    arr[cleanerPos+1].insert(2, 0)
    for i in range(cleanerPos+2, R+1):
        arr[i][C], temp = temp, arr[i][C]
    arr[R].insert(C, temp)
    temp = arr[R].pop(1)
    for i in range(R-1, cleanerPos+1, -1):
        arr[i][1], temp = temp, arr[i][1]

answer = 2 # 공기청정기(-1)가 두 칸있으므로 미리 2에서 시작함
for i in range(1, R+1):
    for j in range(1, C+1):
        answer+=arr[i][j]

print(answer)
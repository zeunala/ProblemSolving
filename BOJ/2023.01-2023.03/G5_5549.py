'''
행성 탐사

입력
첫째 줄에 지도의 크기 M과 N이 주어진다. (1 ≤ M, N ≤ 1000)
둘째 줄에 정인이가 만든 조사 대상 영역의 개수 K가 주어진다. (1 ≤ K ≤ 100000)
셋째 줄부터 M개 줄에는 상근이가 보낸 지도의 내용이 주어진다.
다음 K개 줄에는 조사 대상 영역의 정보가 주어진다. 정보는 네 정수 a b c d로 이루어져 있다.
구역은 직사각형 모양 이며, 왼쪽 위 모서리의 좌표가 (a, b) 오른쪽 아래 모서리의 좌표가 (c, d)이다.

출력
각 조사 대상 영역에 포함되어 있는 정글, 바다, 얼음의 수를 공백으로 구분해 한 줄에 한 정보씩 출력한다.
'''

'''
- 각 구역별로 정글/바다/얼음의 수에 대한 누적 합을 구한다.
* Fail/1st/00:20:39
'''
import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())

arr = []
for i in range(M):
    arr.append(list(sys.stdin.readline().rstrip()))
    
arrJ = [[0 for _ in range(N)] for _ in range(M)]
arrO = [[0 for _ in range(N)] for _ in range(M)]
arrI = [[0 for _ in range(N)] for _ in range(M)]

print(arr)
for i in range(M):
    for j in range(N):
        if arr[i][j] == "J":
            arrJ[i][j] = 1
        elif arr[i][j] == "O":
            arrO[i][j] = 1
        elif arr[i][j] == "I":
            arrI[i][j] = 1

# 누적합 계산
for i in range(M):
    for j in range(1, N):
        arrJ[i][j] += arrJ[i][j - 1]
        arrO[i][j] += arrO[i][j - 1]
        arrI[i][j] += arrI[i][j - 1]
for i in range(1, M):
    for j in range(N):
        arrJ[i][j] += arrJ[i - 1][j]
        arrO[i][j] += arrO[i - 1][j]
        arrI[i][j] += arrI[i - 1][j]
        
# 편의상 0을 맨 왼쪽과 맨 위에 삽입합
for i in range(M):
    arrJ[i] = [0] + arrJ[i]
    arrO[i] = [0] + arrO[i]
    arrI[i] = [0] + arrI[i]
arrJ = [[0 for _ in range(N + 1)]] + arrJ
arrO = [[0 for _ in range(N + 1)]] + arrO
arrI = [[0 for _ in range(N + 1)]] + arrI
        
for i in range(K):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    
    numJ = arrJ[c][d] - arrJ[c][b - 1] - arrJ[a - 1][d] + arrJ[a - 1][b - 1]
    numO = arrO[c][d] - arrO[c][b - 1] - arrO[a - 1][d] + arrO[a - 1][b - 1]
    numI = arrI[c][d] - arrI[c][b - 1] - arrI[a - 1][d] + arrI[a - 1][b - 1]
    
    print(numJ, numO, numI)
'''
나무 재테크

입력
첫째 줄에 N, M, K가 주어진다.

둘째 줄부터 N개의 줄에 A배열의 값이 주어진다.
r번째 줄의 c번째 값은 A[r][c]이다.
다음 M개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x, y, z가 주어진다.
처음 두 개의 정수는 나무의 위치 (x, y)를 의미하고, 마지막 정수는 그 나무의 나이를 의미한다.

출력
첫째 줄에 K년이 지난 후 살아남은 나무의 수를 출력한다.
'''

'''
- 문제의 조건을 그대로 구현하되 시간 초과가 나지 않도록 주의해야 한다.
각 구역에선 나이가 1인 나무가 추가되거나, 양분이 없어 사망하거나 둘 중 하나이므로
deque을 이용해서 나이가 오름차순인 상태가 유지되도록 한다.
* Pass/1st/00:47:42(use PyPy3)
'''
import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().rstrip().split())
arr = [[5 for _ in range(N)] for _ in range(N)] # 현재 땅의 양분의 양
treeArr = [[deque() for _ in range(N)] for _ in range(N)] # 현재 땅의 나무들의 나이들을 오름차순으로 저장
feedArr = [[] for _ in range(N)] # 매 겨울마다 주는 양분의 양

for i in range(N):
    feedArr[i] = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(M):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    
    # (1, 1) -> (0, 0) 좌표 변환
    x -= 1
    y -= 1
    
    treeArr[x][y].append(z)

for i in range(N):
    for j in range(N):
        treeArr[i][j] = deque(sorted(list(treeArr[i][j]))) # 오름차순으로 정렬

for year in range(K): # K년 반복
    # 봄, 여름
    for i in range(N):
        for j in range(N):  
            for k in range(len(treeArr[i][j])):
                if arr[i][j] >= treeArr[i][j][k]: # 양분 있으면 나이+1
                    arr[i][j] -= treeArr[i][j][k]
                    treeArr[i][j][k] += 1
                else: # 중간에 양분이 없다면 treeArr[i][j][k]부터 treeArr[i][j][-1]까지는 전부 사망시키고 성장을 종료한다.
                    for k2 in range(len(treeArr[i][j]) - k):
                        arr[i][j] += (treeArr[i][j].pop() // 2) # 사망하면서 양분증가
                    break

    # 가을
    for i in range(N):
        for j in range(N):
            for k in range(len(treeArr[i][j])): # 각 영역별로 나이가 5의 배수인 것들 확인
                if treeArr[i][j][k] % 5 == 0:
                    for (a, b) in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                        if a >= 0 and a < N and b >= 0 and b < N:
                            treeArr[a][b].appendleft(1)
                    

    # 겨울
    for i in range(N):
        for j in range(N):
            arr[i][j] += feedArr[i][j]

     
answer = 0
for i in range(N):
    for j in range(N):
        answer += len(treeArr[i][j])
print(answer)
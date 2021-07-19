'''
구간 합 구하기 5

입력
첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

출력
총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.
'''

'''
- 우선 표를 하나 더 만들어서 그 표의 (x0, y0)값이 (1,1)부터 (x0, y0)의 값을 가지도록 하자.
그러면 (x1, y1)부터 (x2, y2)까지의 합은 그 표의 (x2, y2) - (x2, y1-1) - (x1-1, y2) + (x1-1, y1-1)의 값이 된다.
* Pass/1st/00:26:17
'''

import sys
N, M = map(int, input().split())
arr = []

# 표 입력받기
arr.append([0]*(N+1)) # 1열부터 시작하기 위함
for i in range(N):
    arr.append([0]+list(map(int, sys.stdin.readline().rstrip().split()))) # 1행부터 시작하기 위함

for i in range(1, N+1):
    for j in range(1, N+1):
        arr[i][j] += arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1] # 누적합을 구함

question = []
for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    question.append((x1, y1, x2, y2))

for i in question:
    (x1, y1, x2, y2) = i
    print(arr[x2][y2]-arr[x2][y1-1]-arr[x1-1][y2]+arr[x1-1][y1-1])
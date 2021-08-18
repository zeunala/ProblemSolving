'''
RGB거리 2

입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
'''

'''
- RGB거리 문제에서 1번집과 N번집 색이 달라야 한다는 조건이 추가되었다.
1번집과 N번집이 (R,G), (R,B), (G,R), (G,B), (B,R), (B,G)인 경우 중 최솟값을 각각 구해보고 이들 중 최솟값을 택하면 될 것이다.
* Pass/1st/00:26:39
'''
import sys
from copy import deepcopy

INF = 9999999

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 먼저 첫번째집이 Red인 경우(첫번째집의 Green/Blue비용을 매우 크게 설정해서 선정되지 않도록 한다. 또한 마지막집이 Red인 집은 최종 후보에서 제외한다)
arrCopy = deepcopy(arr)
arrCopy[0][1] = INF
arrCopy[0][2] = INF

dp = []
dp.append(arrCopy[0])
for i in range(1, N):
    dp.append([min(dp[i-1][1], dp[i-1][2])+arrCopy[i][0], min(dp[i-1][0], dp[i-1][2])+arrCopy[i][1], min(dp[i-1][0], dp[i-1][1])+arrCopy[i][2]])
minR = min(dp[N-1][1], dp[N-1][2])

# 첫번째집이 Green인 경우
arrCopy = deepcopy(arr)
arrCopy[0][0] = INF
arrCopy[0][2] = INF

dp = []
dp.append(arrCopy[0])
for i in range(1, N):
    dp.append([min(dp[i-1][1], dp[i-1][2])+arrCopy[i][0], min(dp[i-1][0], dp[i-1][2])+arrCopy[i][1], min(dp[i-1][0], dp[i-1][1])+arrCopy[i][2]])
minG = min(dp[N-1][0], dp[N-1][2])

# 첫번째집이 Blue인 경우
arrCopy = deepcopy(arr)
arrCopy[0][0] = INF
arrCopy[0][1] = INF

dp = []
dp.append(arrCopy[0])
for i in range(1, N):
    dp.append([min(dp[i-1][1], dp[i-1][2])+arrCopy[i][0], min(dp[i-1][0], dp[i-1][2])+arrCopy[i][1], min(dp[i-1][0], dp[i-1][1])+arrCopy[i][2]])
minB = min(dp[N-1][0], dp[N-1][1])

print(min(minR, minG, minB))
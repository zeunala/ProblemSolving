'''
RGB거리

입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
'''

'''
- N*3의 DP배열을 만들자. dp[n][0]은 n번째 집을 빨강색으로 칠했을 때 n번째까지의 최소 비용값, dp[n][1], dp[n][2]은 각각 초록/파랑색으로 칠한 것과 대응한다.
이 때 dp[n+1][0]은 min(dp[n][1], dp[n][2])+(n+1)번째를 빨강색으로 칠하는 비용과 같은 방식으로 계산할 수 있다.
* Pass/1st/00:27:21
'''

import sys

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split()))) # arr[i]는 i번 집의 [빨강비용, 초록비용, 파랑비용]이다. (편의상 0번 집부터 시작한다고 하자)

dp = []
dp.append([arr[0][0], arr[0][1], arr[0][2]]) # base case

for i in range(1, N):
    dp.append([min(dp[i-1][1],dp[i-1][2])+arr[i][0], min(dp[i-1][0],dp[i-1][2])+arr[i][1], min(dp[i-1][0],dp[i-1][1])+arr[i][2]])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
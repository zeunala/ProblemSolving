'''
디저트

입력
첫 번째 줄에 한 주기의 날짜 수 N (1 ≤ N ≤ 100,000), 디저트 종류의 수 M(1 ≤ M ≤ 10)이 정수로 주어진다.
두 번째 줄부터 M개의 줄에 N개의 자연수 Vij (0 ≤ Vij ≤ 100)가 주어진다.
j (2 ≤ j ≤ M + 1)번째 줄의 i (1 ≤ i ≤ N)번째 자연수 Vij는 i번째 날에 (j – 1)번째 디저트의 만족감을 나타낸다.

출력
한 주기마다 얻을 수 있는 만족감의 최댓값을 출력한다.
단, 각 주기의 첫 날의 만족감은 이전 주기의 마지막 날에 영향을 받지 않으며, 하루에 한 가지의 디저트는 반드시 먹는다.
'''

'''
- DP 문제로 보인다. 첫번째날 부터 하나하나 계산해보자.
* Fail/1st/00:12:15/ValueError
- 디저트가 한 종류일 때 max의 인자가 empty string이 되어 에러가 난다. 이 부분을 처리해보자.
* Pass/2nd/00:15:34
'''
import sys
N, M = map(int, input().split()) # N: 날짜 수, M: 디저트 종류 수
valueArr = [] # valueArr[i][j]는 i번째 디저트를 j번째 날에 먹었을 때 얻는 만족감
for i in range(M):
    valueArr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
dp = [[0 for _ in range(M)] for _ in range(N)] # dp[a][b]는 a번째 날에 b번째 디저트를 먹었을 때 최대 만족감
for j in range(M):
    dp[0][j] = valueArr[j][0]
    
for i in range(1, N):
    for j in range(M):
        dp[i][j] = max(max(dp[i-1][:j]+dp[i-1][j+1:]+[-999999999]) + valueArr[j][i], dp[i-1][j] + valueArr[j][i] // 2)
        
print(max(dp[N-1]))
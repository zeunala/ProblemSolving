'''
제곱수의 합

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

출력
주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.
'''

'''
- 우선 N이하의 모든 제곱수들을 구하고, dp[i]를 i를 나타낼 때 제곱수 항의 최소 개수로 두어 연산한다.
* Pass/1st/00:08:43
'''
import math

N = int(input())
squareArr = [] # N이하의 되는 모든 제곱수

for i in range(1, math.floor(math.sqrt(N) + 1)):
    squareArr.append(i * i)
    
INF = 10 ** 10
dp = [INF] * (N + 1) # dp[i]는 i를 나타낼 때 제곱수 항의 최소 개수
dp[0] = 0

for i in range(1, len(dp)):
    for e in squareArr:
        if i < e:
            break
        dp[i] = min(dp[i], dp[i - e] + 1)

print(dp[N])
'''
동전 1

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
다음 n개의 줄에는 각각의 동전의 가치가 주어진다.
동전의 가치는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다. 경우의 수는 231보다 작다.
'''

'''
- DP를 이용하여 풀면 될 것으로 보인다.
* Fail/1st/00:26:26
'''
n, k = map(int, input().split())
coinPrice = []

for i in range(n):
    coinPrice.append(int(input()))
coinPrice.sort()

dp = [[0 for _ in range(k + 1)] for _ in range(n)] # dp[a][b]는 a번째(a>=0)까지의 동전을 이용해서 b원을 만드는 경우의 수

# dp의 첫번째줄을 채움
i = 0
while coinPrice[0] * i <= k:
    dp[0][coinPrice[0] * i] = 1
    i += 1

# 두번째줄부터 나머지를 채움
for i in range(1, n):
    dp[i][0] = 1
        
    for j in range(1, k + 1):
        if j - coinPrice[i] < 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        else:
            dp[i][j] = dp[i][j - coinPrice[i]] + max(dp[i - 1][j - coinPrice[i]], dp[i - 1][j])
        
print(dp[-1][-1])
'''
동전 1

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
다음 n개의 줄에는 각각의 동전의 가치가 주어진다.
동전의 가치는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다. 경우의 수는 2^31보다 작다.
'''

'''
- DP를 이용하여 풀면 될 것으로 보인다.
* Fail/1st/00:26:26
- 메모리초과를 막도록 dp를 두 줄만 사용하도록 수정하였다.
* Fail/2nd/00:31:28
- dp갱신하는 부분을 일부 수정하였다.
* Pass/3rd/00:50:12
'''
n, k = map(int, input().split())
coinPrice = []

for i in range(n):
    coinPrice.append(int(input()))
coinPrice.sort()

dp = [0] * (k + 1) # dp[a]는 동전을 이용해서 a원을 만드는 경우의 수
dpPrev = [] # 이전 dp 저장

# 첫번째 동전만을 사용하는 경우를 채움
i = 0
while coinPrice[0] * i <= k:
    dp[coinPrice[0] * i] = 1
    i += 1

# 두번째줄부터 나머지를 채움
for i in range(1, n):
    dpPrev = dp[:]
    dp = [0] * (k + 1)
    
    dp[0] = 1
        
    for j in range(1, k + 1):
        if j - coinPrice[i] < 0:
            dp[j] = max(dp[j], dpPrev[j])
        else:
            dp[j] = dp[j - coinPrice[i]] + dpPrev[j]
        
print(dp[-1])
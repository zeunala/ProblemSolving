'''
평범한 배낭

입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
입력으로 주어지는 모든 수는 정수이다.

출력
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
'''

'''
- 물건의 수가 100개라 완전 탐색은 어렵고 최대 가능 무게가 1일 때부터 차례로 탐색하며 각 무게에 대한 최대 가치합을 구해보자.
* Fail/1st/00:22:21
'''

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = [] # [무게, 가치]들의 배열들
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0 , []] for _ in range(K+1)] # dp[N][0]은 최대 무게제한이 N일 때의 최대 가치합이다. dp[N][1]은 그 때의 넣은 물건들의 인덱스이다.
for i in range(1, K+1):
    for j in range(len(arr)):
        if i < arr[j][0]: # 무게 초과시
            continue
        elif (dp[i-arr[j][0]][0]+arr[j][1] > dp[i][0]) and (j not in dp[i-arr[j][0]][1]): # 기존 최대 가치합보다 이 물건을 넣었을 때 가치합 최대일 때(이 때 물건 중복해서 들어가면 안 됨)
            dp[i][0] = dp[i-arr[j][0]][0]+arr[j][1]
            dp[i][1] = dp[i-arr[j][0]][1] + [j]
        
        if dp[i][0] < dp[i-1][0]: # 이전 무게가 오히려 더 나은 경우
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1]


print(dp[K][0])
'''
상자넣기

입력
파일의 첫 번째 줄은 상자의 개수 n (1 ≤ n ≤ 1000)을 나타낸다.
두 번째 줄에는 각 상자의 크기가 순서대로 주어진다.
상자의 크기는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 한 줄에 넣을 수 있는 최대의 상자 개수를 출력한다.
'''

'''
- 총 상자의 개수가 n개일 때 이차원 배열 arr[n+1][1001]을 만들어
arr[i][j]는 i번째까지 j일때 뒤에 몇 개의 상자를 더 넣을 수 있는지 저장하도록 한다.
* Pass/1st/00:16:17
'''
import sys

n = int(sys.stdin.readline().rstrip())
arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[0 for _ in range(1001)] for _ in range(len(arr) + 1)]

for i in range(len(arr) - 2, -1, -1):
    for j in range(1001):
        if arr[i+1] > j:
            dp[i][j] = max(dp[i+1][j], dp[i+1][arr[i+1]] + 1)
        else:
            dp[i][j] = dp[i+1][j]

print(dp[0][0])
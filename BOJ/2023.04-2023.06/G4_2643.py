'''
색종이 올려 놓기

입력
첫 번째 줄에는 색종이의 장수가 주어진다. 다음 줄부터 각 줄에 색종이의 두 변의 길이가 주어진다.
두 변의 길이는 한 칸 띄어 주어진다. 색종이의 최대 장수는 100이고, 각 변의 길이는 1000보다 작은 자연수이다.

출력
쌓을 수 있는 최대 색종이 장수를 출력한다.
'''

'''
- 가로와 세로 길이가 일정 또는 감소하도록 차례로 쌓아야 한다.
우선 가로 길이를 오름차순으로 정렬하고, 세로 길이만 보는 문제로 변환한다.
이때 각 정사각형을 가로 길이가 더 큰 방향으로 통일시킨다.
* Pass/1st/00:45:13
'''
import sys

MAX_LENGTH = 1000

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a < b:
        a, b = b, a
    arr.append((a, b))
arr.sort()

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[i][1] >= arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
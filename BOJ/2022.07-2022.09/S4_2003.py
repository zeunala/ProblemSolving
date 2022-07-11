'''
수들의 합 2

입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다.
다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다.
각각의 A[x]는 30,000을 넘지 않는 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다.
'''

'''
- 투 포인터 문제이다. M이 될 때마다 카운팅 하는 방식으로 총 경우의 수를 셀 수 있다.
* Pass/1st/00:05:02
'''
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = 0
arrSum = arr[0]
answer = 0

while start < N:
    if arrSum == M:
        answer += 1
        arrSum -= arr[start]
        start += 1
    elif arrSum > M:
        arrSum -= arr[start]
        start += 1
    elif arrSum < M:
        end += 1
        if end >= N:
            break
        arrSum += arr[end]
        
print(answer)
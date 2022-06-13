'''
구간 합 구하기 4

- 입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다.
둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다.
셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
'''

'''
- 누적 합을 미리 구해놓으면 되는 문제로 보인다.
* Pass/1st/00:03:37
'''
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = [0] + arr

arrSum = [0]
for i in range(1, len(arr)):
    arrSum.append(arrSum[i - 1] + arr[i])

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(arrSum[b] - arrSum[a - 1])
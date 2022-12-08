'''
K번째 수

입력
첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
둘째에는 A1, A2, ..., AN이 주어진다. (-10^9 ≤ Ai ≤ 10^9)

출력
A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.
'''

'''
- 퀵 소트 때와 비슷하게 임의의 수 하나를 잡고 그 수보다 작은 그룹과 큰 그룹으로 묶는다.
* Fail/1st/00:20:27
- 재귀호출을 사용하지 않는 방향으로 진행한다.
* Fail/2nd/00:26:13/TimeOver
- 파이썬의 sort를 그대로 이용하는 방법으로 시도해본다.
* Pass/3rd/00:37:26
'''
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
print(arr[K - 1])
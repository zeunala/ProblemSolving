'''
카드 게임

입력
첫째 줄에 세 개의 자연수 N, M, K가 주어진다. (1 ≤ M ≤ N ≤ 4,000,000, 1 ≤ K ≤ min(M, 10,000))
다음 줄에 카드의 번호를 나타내는 M개의 자연수가 주어진다. 각각의 수들은 1 이상이고 N 이하이며 서로 다르다.
다음 줄에 K개의 자연수가 주어진다. i번째 수는 철수가 i번째로 내는 카드의 번호이다. 철수가 내는 카드 역시 1 이상 N 이하이다.

출력
K줄에 걸쳐서 수를 출력한다. i번째 줄에는 민수가 i번째로 낼 카드의 번호가 출력되어야 한다.
'''

'''
- 1~400만중 현재 민수가 보유한 카드들을 배열로 저장한다. 매 숫자에 대해 그 숫자를 초과하는 가장 작은 수를 찾아야한다.
배열에서 보유 중인 숫자는 False로, 보유하지 않는다면 몇 번째 뒤의 숫자를 찾으면 될지 숫자로 저장한다.
예를 들어 1,2,3,4,5중 1,4 만을 가지고 있다면 [False, 2, 1, False, 1]와 같이 저장하고 (마지막 인덱스는 임의)
2보다 큰 수를 보유하고 있는지 찾으려면 arr[2] 탐색 -> arr[2]가 2이므로 arr[2+2]탐색과 같은 방식으로 찾는다.
* Fail/1st/00:22:01/TimeLimitExceeded
'''
import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
inputArr = list(map(int, sys.stdin.readline().rstrip().split())) # 현재 보유한 카드 번호들
minsuArr = list(map(int, sys.stdin.readline().rstrip().split())) # 민수가 낼 카드 번호들

arr = [1] * (N + 1)

for e in inputArr:
    arr[e] = False

idx = 1
for i in range(len(arr) - 1, -1, -1):
    if arr[e] == False:
        idx = 1
    else:
        arr[e] = idx
        idx += 1

for num in minsuArr:
    target = num + 1 # 이 번호가 있는지 탐색하고, 없으면 그 다음 번호를 찾음
    while arr[target] != False: # 민수가 카드를 내지 못하는 경우는 없으므로 반드시 target값이 존재한다.
        target += arr[target]
    print(target)
    arr[target] = 1
'''
N과 M (9)

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

'''
- 그냥 permutations 이용하면 될 것이다. 중복되는 수열을 여러 번 출력하면 안된다는 점과 사전 순으로 증가해야 한다는 것만 주의하자.
* Pass/1st/00:09:25
'''
from itertools import permutations

N, M = map(int, input().split()) # N개의 자연수 중 M개를 고른 수열
arr = map(int, input().split())

allAnswer = list(set(permutations(arr, M))) # set으로 감싸 중복되는 수열 제거
allAnswer.sort() # 사전순 증가

for e in allAnswer:
    for e2 in e:
        print(e2, end=" ")
    print()
'''
과일 서리

입력
첫째 줄에 과일의 종류 수 N(1 ≤ N ≤ 10)이 주어진다.
둘째 줄에 훔치려 하는 과일의 개수 M(N ≤ M ≤ 30)이 주어진다.

출력
첫째 줄에 훔칠 수 있는 경우의 수를 출력한다.
'''

'''
- 모든 과일을 1개씩은 훔쳐야하므로 (N)H(M-N)의 중복조합 문제로 풀면 된다.
* Pass/1st/00:07:46
'''
import math

def calcH(n, r): # nHr계산
    return math.comb(n + r - 1, r)

N = int(input())
M = int(input())

if N > M:
    print(0)
else:
    print(calcH(N, M - N))
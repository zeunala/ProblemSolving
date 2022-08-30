'''
다리 놓기

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)이 주어진다.

출력
각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력한다.
'''

'''
- mCn을 구하면 되는 문제이다.
* Pass/1st/00:04:05
- 처음에는 from itertools import combinations를 이용하려고 했으나 math를 이용해서 더 간단히 계산할 수 있음을 알게 되었던 문제였다.
'''
import math

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    print(math.comb(M, N))
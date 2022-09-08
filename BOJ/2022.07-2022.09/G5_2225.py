'''
합분해

입력
첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

출력
첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''

'''
- 문제를 조금 바꾸면 1~N까지의 정수 K개를 더해 합이 N+K가 되는 경우의 수를 구하면 된다.
이를 N+K개의 블록이 나열되었을 때, 그 사이에 칸 막이를 K-1개 넣는 경우의 수와 같으며 이는 (n+K-1)C(k-1)이다.
* Pass/1st/00:04:49
'''
import math

N, K = map(int, input().split())
print(math.comb(N+K-1, K-1) % 1000000000)
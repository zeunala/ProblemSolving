'''
듣보잡

입력
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

출력
듣보잡의 수와 그 명단을 사전순으로 출력한다.
'''

'''
- 파이썬의 집합 자료형을 이용하여 쉽게 구할 수 있다.
* Pass/1st/00:03:11
'''
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
case1 = set() # 듣도 못한 사람들의 집합
case2 = set() # 보도 못한 사람들의 집합

for i in range(N):
    case1.add(sys.stdin.readline().rstrip())
for i in range(M):
    case2.add(sys.stdin.readline().rstrip())

answer = list(case1.intersection(case2))
answer.sort()

print(len(answer))
for e in answer:
    print(e)
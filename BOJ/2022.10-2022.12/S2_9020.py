'''
골드바흐의 추측

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

출력
각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다.
출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.
'''

'''
- n의 범위가 최대 1만까지이므로 모든 소수의 목록을 구해 각 케이스별 O(n)으로 파티션을 구하도록 한다.
* Pass/1st/00:07:45
'''
import sys

T = int(sys.stdin.readline().rstrip())

primeSet = set() # 1만까지의 모든 소수가 여기 담기도록 함

primeArr = [True] * 10001
primeArr[0] = False
primeArr[1] = False
for i in range(2, len(primeArr)):
    if primeArr[i]:
        primeSet.add(i)
        j = 2
        while i * j < len(primeArr):
            primeArr[i * j] = False
            j += 1

for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    
    for j in range(n // 2, 0, -1):
        if j in primeSet and (n - j) in primeSet:
            print(j, n - j)
            break
'''
대칭 차집합

입력
첫째 줄에 집합 A의 원소의 개수와 집합 B의 원소의 개수가 빈 칸을 사이에 두고 주어진다.
둘째 줄에는 집합 A의 모든 원소가, 셋째 줄에는 집합 B의 모든 원소가 빈 칸을 사이에 두고 각각 주어진다.
각 집합의 원소의 개수는 200,000을 넘지 않으며, 모든 원소의 값은 100,000,000을 넘지 않는다.

출력
첫째 줄에 대칭 차집합의 원소의 개수를 출력한다.
'''

'''
- 파이썬의 집합 자료형을 이용하여 쉽게 계산할 수 있다.
* Pass/1st/00:02:58
'''
import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
arrA = set(map(int, sys.stdin.readline().rstrip().split()))
arrB = set(map(int, sys.stdin.readline().rstrip().split()))

print(len(arrA) + len(arrB) - (2 * len(arrA.intersection(arrB))))
'''
30번

입력
첫 번째 줄에 테스트 케이스의 수 T (1 ≤ T ≤ 50000)가 주어진다. 이후 T개의 테스트 케이스가 주어진다.
각 테스트 케이스는 한 줄로 구성되어 있으며, 각 줄에는 두 개의 정수 A와 B (1 ≤ A, B ≤ 1023, A ≠ B)가 공백을 사이로 두고 주어진다.
이는 첫 번째 빈 칸에는 A를, 두 번째 빈 칸에는 B를 넣었을 때 답을 구하라는 의미이다.

출력
각 테스트 케이스에 대해 답을 한 줄에 하나씩 출력한다.
'''

'''
- 꼭지점 x의 부모는 x/2임을 이용하여, M(a, b)에서 a와 b 각각 부모로 가는 경로를 구하고, 이들중 최댓값을 찾는다.
* Pass/1st/00:07:46
'''
import sys

def solution(a, b): # M(a, b)값 계산
    setA = set() # A에서 1까지 가는 경로들
    setB = set() # B에서 1까지 가는 경로들
    
    while a > 0:
        setA.add(a)
        a //= 2
    while b > 0:
        setB.add(b)
        b //= 2
        
    return max(setA.intersection(setB))
    
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(10 * solution(A, B))
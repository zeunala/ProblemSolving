'''
서로소 쌍

입력
첫 번째 줄에 테스트 케이스의 개수를 나타내는 자연수 T가 주어진다.
다음 줄부터 차례로 T개의 테스트 케이스가 주어진다.
각각의 테스트 케이스의 첫째 줄에 100,000,000이하의 자연수 N이 주어진다.

출력
각 테스트 케이스의 답을 순서대로 출력한다.
각 테스트 케이스마다 첫 줄에 N을 최소공배수로 하는 서로소인 자연수 쌍의 개수를 한 줄에 하나씩 출력한다.
'''

'''
- N의 범위가 1억이하이므로 우선 A * B = N이 되는 A, B쌍을 모두 찾고, A와 B가 서로소인 경우 체크하여 총 개수를 확인한다.
* Pass/1st/00:04:53
'''
import math

def solution(num):
    answer = 0
    for A in range(1, math.floor(math.sqrt(num)) + 1):
        if num % A != 0:
            continue
        B = N // A
        if math.gcd(A, B) == 1:
            answer += 1
    return answer

T = int(input())
for i in range(T):
    N = int(input())
    print(solution(N))
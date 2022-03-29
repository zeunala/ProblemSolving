'''
소수의 배수

입력
첫째 줄에 N(1 ≤ N ≤ 10)과 M(1 ≤ M ≤ 10^12)이 주어진다.
둘째 줄에는 N개의 소수가 주어진다. 입력으로 주어지는 소수는 100보다 작거나 같으며, 같은 소수가 두 번 이상 주어지지 않는다.

출력
첫째 줄에 M 이하의 자연수 중에서 N개의 소수 중 적어도 하나로 나누어 떨어지는 수의 개수를 출력한다.
'''

'''
- 합집합 = 각각의 원소의 개수 - 교집합 의 개념에서 접근해, 홀수개를 택한 것들의 곱의 경우를 더하고 짝수개를 택한 것들의 곱의 경우를 빼주자.
* Pass/1st/00:07:31
'''
from itertools import combinations

def allProduct(list):
    result = 1
    for e in list:
        result *= e
    return result

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
for i in range(1, N+1):
    for case in list(combinations(arr, i)):
        if i % 2 == 1: # 홀수개 택한 것들의 곱의 경우를 더함
            answer += M // allProduct(case)
        else: # 짝수개 택한 것들의 곱의 경우를 뺌
            answer -= M // allProduct(case)
            
print(answer)
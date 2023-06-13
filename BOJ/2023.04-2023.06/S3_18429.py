'''
근손실

입력
첫째 줄에 자연수 N과 K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 8, 1 ≤ K ≤ 50)
둘째 줄에 각 운동 키트의 중량 증가량 A가 공백을 기준으로 구분되어 주어진다. (1 ≤ A ≤ 50)

출력
N일 동안 N개의 운동 키트를 사용하는 모든 경우 중에서, 운동 기간동안 항상 중량이 500 이상이 되도록 하는 경우의 수를 출력한다.
'''

'''
- N의 범위가 작으므로 모든 경우의 수를 탐색한다.
* Pass/1st/00:04:53
'''
from itertools import permutations

def isValid(arr, case, K):
    current = 500
    
    for e in case:
        current += arr[e]
        current -= K
        
        if current < 500:
            return False
    return True

N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
for case in permutations(range(N), N):
    if isValid(arr, case, K):
        answer += 1
print(answer)
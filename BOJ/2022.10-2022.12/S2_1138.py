'''
한 줄로 서기

입력
첫째 줄에 사람의 수 N이 주어진다. N은 10보다 작거나 같은 자연수이다.
둘째 줄에는 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지 주어진다.
i번째 수는 0보다 크거나 같고, N-i보다 작거나 같다. i는 0부터 시작한다.

출력
첫째 줄에 줄을 선 순서대로 키를 출력한다.
'''

'''
- N의 범위가 적으므로 모든 경우의 수를 다 체크한다.
* Fail/1st/00:16:22/MemoryLimitExceeded
'''
from itertools import permutations

N = int(input())
allCase = list(permutations(range(1, N + 1), N))
arr = list(map(int, input().split()))

result = None
for case in allCase:
    valid = True
    for i in range(N): # 현재 서있는 사람의 첫번째부터 조건에 맞는지 검증
        currentRank = len([j for j in case[:i] if j > case[i]])
        if currentRank == arr[case[i] - 1]:
            continue
        else:
            valid = False
            break
    if valid:
        result = case
        break
    
answer = ""
for e in result:
    answer += str(e) + " "
    
print(answer[:-1])
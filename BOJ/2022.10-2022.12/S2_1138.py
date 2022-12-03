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
- 메모리 제한으로 인해 dfs방식을 이용하도록 수정하였다.
* Pass/2nd/00:26:18(use PyPy3)
- 문제 풀이 이후 다른 사람의 풀이를 본 결과,
우선 0으로 자리만 만들고 가장 작은 사람부터 왼쪽 0의 개수를 보고 배치하는 그리디 알고리즘 방식이 가능함을 알게 되었다.
'''
result = None

def dfs(arr, case, remainNum):
    global result
    if result != None:
        return
    
    if len(remainNum) == 0:
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
        
    for i in range(len(remainNum)):
        dfs(arr, case + [remainNum[i]], remainNum[:i] + remainNum[i + 1:])

N = int(input())
arr = list(map(int, input().split()))

dfs(arr, [], [i for i in range(1, N + 1)])
    
answer = ""
for e in result:
    answer += str(e) + " "
    
print(answer[:-1])
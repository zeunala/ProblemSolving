'''
N-Queen

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다
'''

'''
(과거풀이이력)
* Fail/1st/00:30:31/MemoryOverflow
* Fail/2nd/01:00:44/TimeOver

- 퀸은 각각 서로 다른 행에 1개씩 놔두어야 하므로, 1행부터 놓는다고 치고 순서대로 몇열에 위치하는지 기록해두자.
이 때 기록할 때 같은 열에 퀸이 중복될 수 없으므로 열들이 서로 달라야 하며 대각선도 고려하여야 한다.
* Pass/3rd/01:55:04(use PyPy3)
- N이 작을 때 정답을 구하는 건 쉬웠으나,
어떻게 해도 13부터는 시간이 너무 오래걸려서 이것저것 최적화를 해보다가 포기했었다. (열번호 경우의 수가 많아 메모이제이션을 쓸 수도 없었다)
그런데 이후 다른 사람들의 답안을 찾아보니 동일한 풀이방법을 썼음에도 C++등으로 작성해서 시간초과가 나지 않은 걸 볼 수 있었고,
중도포기 당시 코드를 그대로 PyPy3으로 채점했더니 맞은 것을 확인할 수 있었다.
결국 파이썬 속도의 한계로 인해 동일한 풀이방법을 썼음에도 다른 언어와 달리 시간초과가 나는 것이었고, 백트래킹 문제가 파이썬에게 불리하다는 것을 배울 수 있었다.
'''
answer = 0

def checkQueen(arr, arrLen, N): # arr은 현재까지 퀸이 놓인 열번호, arrLen은 현재까지 퀸이 놓인 수, N은 앞으로 더 놓아야 하는 퀸의 수
    if N == 0:
        global answer
        answer += 1
        return
    
    column = arrLen + N # 총 열 수
    
    possiblePosition = [True] * column # 퀸이 갈 수 있는 열번호를 True로 표기
    for i in range(arrLen):
        possiblePosition[arr[i]] = False # 열번호가 겹치면 안 됨
        if arr[i]+(arrLen-i) < column:
            possiblePosition[arr[i]+(arrLen-i)] = False # 대각선으로도 겹치면 안 됨(오른쪽 대각선방향)
        if arr[i]-(arrLen-i) >= 0:
            possiblePosition[arr[i]-(arrLen-i)] = False # 대각선으로도 겹치면 안 됨(왼쪽 대각선방향)

    for i in range(column): # 0열부터 체크
        if possiblePosition[i]:
            checkQueen(arr+[i], arrLen+1, N-1)


N = int(input())
checkQueen([], 0, N)
print(answer)
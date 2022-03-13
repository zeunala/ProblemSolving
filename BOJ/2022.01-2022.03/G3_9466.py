'''
텀 프로젝트

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다.
각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)

출력
각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.
'''

'''
- 1번 학생부터 탐색해서 본인을 선택하거나 싸이클이 만들어진다면 프로젝트 팀에 속한 걸로 표시한다.
만약 중간에 프로젝트 팀에 속하지 못한 시작점 이전 번호의 사람으로 돌아가거나,
싸이클에 본인이 들어가지 않다면 프로젝트 팀에 속하지 못하게 된다.
이 때, 1번부터 시작하되 중간에 탐색한 것이 있다면 그 번호는 건너뛰어야 시간초과를 방지할 수 있을 것이다.
(예를 들어 5만~10만까지 싸이클을 이루고 있는데 1번~49999번까지 5만을 가리킬 경우 시간초과가 날 것이다.)
* Fail/1st/00:44:50/TimeOver
'''
import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split())) # arr[i]: i+1번 학생이 가리킨 번호
    
    for j in range(len(arr)): # 1~n번을 0~(n-1)번으로 변경
        arr[j] -= 1
    
    visited = [False] * n # visited[i]: i+1번 학생의 조건 탐색 여부
    isTeam = [False] * n # isTeam[i]: i+1번 학생이 프로젝트 팀에 속하는지 여부
    
    for j in range(n):
        if visited[j]:
            continue
        
        if arr[j] == j: # 자기자신 가리키는 경우
            isTeam[j] = True
            visited[j] = True
            continue
        
        cycleArr = [] # 싸이클 후보 순서가 여기 담김
        cycleDict = {} # 싸이클 후보에 속하는지 여부를 빠르게 찾기 위해 사용
        
        # j와 arr[j]부터 싸이클 시작
        cycleArr.append(j)
        cycleArr.append(arr[j])
        cycleDict[j] = True
        cycleDict[arr[j]] = True
        
        while True:
            if visited[cycleArr[-1]] and not isTeam[cycleArr[-1]]: # 현재 있는 싸이클 후보들이 모두 속하지 못하는 경우
                while cycleArr:
                    temp = cycleArr.pop()
                    visited[temp] = True
                break
            if cycleArr[-1] == cycleArr[0]: # 싸이클이 정상적으로 이루어짐
                while cycleArr:
                    temp = cycleArr.pop()
                    visited[temp] = True
                    isTeam[temp] = True
                break
            elif cycleArr[-1] in cycleDict and cycleArr.index(cycleArr[-1]) != len(cycleArr) - 1: # 1 -> 2 -> 3 -> 4 -> 2 와 같이 싸이클이 중간에 만들어지는 경우
                isNotCycle = cycleArr[:cycleArr.index(cycleArr[-1])] # 싸이클 이뤄지지 않은 부분은 팀을 못 이룸
                isCycle = cycleArr[cycleArr.index(cycleArr[-1]):] # 싸이클 이뤄진 부분끼리만 팀을 이룸
                while isNotCycle:
                    temp = isNotCycle.pop()
                    visited[temp] = True
                while isCycle:
                    temp = isCycle.pop()
                    visited[temp] = True
                    isTeam[temp] = True
                break
            else:
                next = arr[cycleArr[-1]]
                cycleArr.append(next)
                cycleDict[next] = True
                
    answer = 0
    for e in isTeam:
        if e == False:
            answer += 1
    print(answer)
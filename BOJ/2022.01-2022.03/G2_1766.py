'''
입력
첫째 줄에 문제의 수 N(1 ≤ N ≤ 32,000)과 먼저 푸는 것이 좋은 문제에 대한 정보의 개수 M(1 ≤ M ≤ 100,000)이 주어진다.
둘째 줄부터 M개의 줄에 걸쳐 두 정수의 순서쌍 A,B가 빈칸을 사이에 두고 주어진다.
이는 A번 문제는 B번 문제보다 먼저 푸는 것이 좋다는 의미이다.
항상 문제를 모두 풀 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 문제 번호를 나타내는 1 이상 N 이하의 정수들을 민오가 풀어야 하는 순서대로 빈칸을 사이에 두고 출력한다.
'''

'''
- 위상정렬 문제로 보인다. 나중에 풀어야 한다는 조건이 없는 것 중 번호가 가장 작은 것부터 풀도록 한다.
* Pass/1st/00:29:20(use PyPy3)
- 다른 사람의 풀이를 보며 굳이 beforeArr, afterArr로 나누지 않고 beforeArr만 두고 진입차수 배열만 따로 두면 되며,
visited 배열도 따로 만들 필요 없다는 것을 알게 되었다.
'''
import sys
import heapq

N, M = map(int, sys.stdin.readline().rstrip().split())
beforeArr = [[] for _ in range(N+1)] # beforeArr[i]는 i번 이전에 풀어야 하는 문제 번호들의 리스트
afterArr = [[] for _ in range(N+1)] # afterArr[i]는 i번 이후에 풀어야 하는 문제 번호들의 리스트

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    beforeArr[b].append(a) # b번 이전에 a번을 풀어야 한다.
    afterArr[a].append(b) # a번 이후에 b번을 풀어야 한다.
    
visited = [True] + [False for _ in range(N)] # visited[i]는 i번 문제를 풀었는지 유무
questionQueue = []

for i in range(len(beforeArr)):
    if len(beforeArr[i]) == 0: # 나중에 풀어야 하는 조건이 없는 문제 번호들
        heapq.heappush(questionQueue, i)

result = "" # 정렬 순서
while questionQueue:
    temp = heapq.heappop(questionQueue)
    if visited[temp]:
        continue
    visited[temp] = True
    
    result += str(temp) + " " # temp번을 푼다
    
    for e in afterArr[temp]: # temp번 이후에 풀어야하는 문제들에 대해 그 조건을 제거
        if temp in beforeArr[e]:
            beforeArr[e].remove(temp)
            if len(beforeArr[e]) == 0: # 만약 제거 했을 때 조건이 아무것도 없어진다면 새로 큐에 들어감
                heapq.heappush(questionQueue, e)
     
print(result[:-1])
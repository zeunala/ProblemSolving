'''
LCA

첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다.
그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.

출력
M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.
'''

'''
- 각 노드별로 parent의 노드번호와 depth를 저장하도록 한다.
* Fail/1st/00:16:10
- 트리를 만드는 과정에서 큐를 이용하여 만들어나가도록 수정하였다.
* Pass/2nd/00:29:19(use PyPy3)
'''
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
parentArr = [0] * (N + 1) # parentArr[i]는 i의 parent 번호 저장
depthArr = [0] * (N + 1) # depthArr[i]는 i의 depth를 저장 (루트가 0)
edgeArr = [[] for _ in range(N + 1)] # edgeArr[i]는 i번 노드와 연결된 노드번호들이 저장됨
visited = [False] * (N + 1)

for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edgeArr[a].append(b)
    edgeArr[b].append(a)
    
tempDeque = deque()
tempDeque.append((1, 0)) # 루트 노드

while tempDeque:
    node, parents = tempDeque.popleft()
    if visited[node]:
        continue
    
    visited[node] = True
    parentArr[node] = parents
    depthArr[node] = depthArr[parents] + 1
    
    for e in edgeArr[node]:
        if not visited[e]:
            tempDeque.append((e, node))
    
M = int(sys.stdin.readline().rstrip())
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
    # 우선 depth를 맞춰준다.
    while depthArr[a] > depthArr[b]:
        a = parentArr[a]
    while depthArr[a] < depthArr[b]:
        b = parentArr[b]
    
    # 공통 조상이 나올 때까지 맞춰준다.
    while a != b:
        a = parentArr[a]
        b = parentArr[b]
        
    print(a)
    
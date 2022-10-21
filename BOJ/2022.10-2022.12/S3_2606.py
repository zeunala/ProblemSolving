'''
바이러스

입력
첫째 줄에는 컴퓨터의 수가 주어진다.
컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
'''

'''
- BFS나 DFS로 컴퓨터를 방문해서 체크하면 될 것으로 보인다.
* Pass/1st/00:05:31
'''
from collections import deque

N = int(input())
K = int(input())
connectArr = [[] for _ in range(N + 1)] # connectArr[i]는 i와 연결된 컴퓨터들의 목록

for i in range(K):
    a, b = map(int, input().split())
    connectArr[a].append(b)
    connectArr[b].append(a)
    
tempQueue = deque() # 앞으로 방문할 컴퓨터 목록
visited = set() # 이미 큐에 넣은 컴퓨터 목록

tempQueue.append(1) # 1번 컴퓨터를 감염
visited.add(1)

while tempQueue:
    temp = tempQueue.popleft()
    
    for e in connectArr[temp]:
        if e not in visited:
            visited.add(e)
            tempQueue.append(e)

print(len(visited) - 1) # 1번 컴퓨터를 제외하고 추가로 감염된 컴퓨터 수
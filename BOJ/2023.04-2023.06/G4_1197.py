'''
최소 스패닝 트리

입력
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다.
다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다.
이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.
그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다.
최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
'''

'''
- 가중치가 작은 것부터 나열하고, 사이클이 생기지 않는 범위에서 그리디 알고리즘으로 간선들을 취한다.
* Fail/1st/00:15:11
'''
import sys
sys.setrecursionlimit(100000)

def findParent(parent, i):
    if parent[i] == i:
        return i
    parent[i] = findParent(parent, parent[i])
    return parent[i]
    
def union(parent, a, b):
    if a > b:
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]

V, E = map(int, sys.stdin.readline().rstrip().split())
graph = [] # (가중치, 시작점, 도착점)으로 구성. 시작점의 번호가 더 작도록 한다.
parent = [i for i in range(V + 1)]

for i in range(E):
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    if A > B:
        A, B = B, A
    graph.append((C, A, B))
    
graph.sort()
answer = 0
for (cost, start, end) in graph:
    if findParent(parent, start) == findParent(parent, end):
        continue
    
    answer += cost
    union(parent, start, end)
    
print(answer)
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
'''
import sys

N = int(sys.stdin.readline().rstrip())
parentArr = [0] * (N + 1) # parentArr[i]는 i의 parent 번호 저장
depthArr = [0] * (N + 1) # depthArr[i]는 i의 depth를 저장 (루트가 0)
inputArr = []

for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    inputArr.append((a, b))
    
inputArr.sort()
for (a, b) in inputArr:
    if parentArr[b] != 0: # 이미 b의 부모가 있을 경우 a, b 순서를 바꿔야 한다.
        a, b = b, a
    parentArr[b] = a
    depthArr[b] = depthArr[a] + 1
    
    
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
    
'''
저울

입력
첫 줄에는 물건의 개수 N 이 주어지고, 둘째 줄에는 미리 측정된 물건 쌍의 개수 M이 주어진다.
단, 5 ≤ N ≤ 100 이고, 0 ≤ M ≤ 2,000이다.
다음 M개의 줄에 미리 측정된 비교 결과가 한 줄에 하나씩 주어진다.
각 줄에는 측정된 물건 번호를 나타내는 두 개의 정수가 공백을 사이에 두고 주어지며, 앞의 물건이 뒤의 물건보다 더 무겁다.

출력
여러분은 N개의 줄에 결과를 출력해야 한다.
i 번째 줄에는 물건 i 와 비교 결과를 알 수 없는 물건의 개수를 출력한다.
'''

'''
- front, back 배열을 만들어 front[i]는 i번 물건보다 앞에 있는(무거운) 물건 번호,
back[i]는 i번 물건보다 뒤에 있는(가벼운) 물건 번호들이 오도록 만들어보자.
물건 i와 비교 결과를 알 수 있는 물건은 front[i] 방향으로 계속해서 탐색하거나 back[i]를 계속해서 탐색해서 나오는 번호일 것이다.
* Fail/1st/00:30:07/TimeOver
'''
from collections import deque
import sys

sys.setrecursionlimit(10000)

def frontDfs(target, current, front, canKnow): # front를 dfs방식으로 탐색. target보다 front에 있는 걸 전부 탐색한다.
    # 1>2, 1>4>2>3 과 같은 경우가 있을 수 있기에 이미 방문한 노드도 끝까지 탐색한다.
    # 어차피 모순된 입력은 주어지지 않으므로 사이클 등 무한루프에 빠질 염려는 하지 않아도 된다.
    for e in front[current]:
        canKnow[target][e] = True
        canKnow[e][target] = True
        frontDfs(target, e, front, canKnow)
        
def backDfs(target, current, front, canKnow): # back을 dfs방식으로 탐색. target보다 back에 있는 걸 전부 탐색한다.
    for e in front[current]:
        canKnow[target][e] = True
        canKnow[e][target] = True
        frontDfs(target, e, front, canKnow)

N = int(input()) # 물건의 개수
M = int(input()) # 미리 측정된 물건 쌍의 개수
front = [[] for _ in range(N+1)] # front[i]는 i번 물건보다 앞에 있는(무거운) 물건 번호
back = [[] for _ in range(N+1)] # back[i]는 i번 물건보다 뒤에 있는(가벼운) 물건 번호
canKnow = [[False for _ in range(N+1)] for _ in range(N+1)] # canKnow[a][b]는 물건 a와 물건 b를 비교할 수 있는지 여부
for i in range(N+1):
    canKnow[i][0] = True
    canKnow[i][i] = True

for i in range(M):
    big, small = map(int, input().split())
    front[small].append(big)
    back[big].append(small)

for i in range(1, N+1): # front, back을 dfs방식으로 탐색
    frontDfs(i, i, front, canKnow)
    backDfs(i, i, front, canKnow)
    
for i in range(1, N+1):
    temp = 0
    for e in canKnow[i]:
        if e == False:
            temp += 1
    print(temp)
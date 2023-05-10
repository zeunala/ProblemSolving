'''
점프 점프

입력
첫 번째 줄에는 돌다리의 돌 개수 n이 주어진다.(1≤n≤100,000) 돌의 번호는 왼쪽부터 1번에서 n번이다.
다음 줄에는 그 위치에서 점프할 수 있는 거리 Ai가 주어진다.(1≤Ai≤100,000)
다음 줄에는 출발점 s가 주어진다.(1≤s≤n)

출력
영우가 방문 가능한 돌들의 개수를 출력하시오.
'''

'''
- BFS를 이용하여 모든 경우의 수를 탐색하도록 한다.
* Pass/1st/00:05:50
'''
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
s = int(sys.stdin.readline().rstrip())

s -= 1 # 편의상 돌 번호를 0번부터 시작하도록 한다.

visited = set()
currentQueue = deque()

visited.add(s)
currentQueue.append(s)

while currentQueue:
    current = currentQueue.popleft()
    
    next1 = current + arr[current] # 앞으로 가는 경우
    next2 = current - arr[current] # 뒤로 가는 경우
    
    if next1 >= 0 and next1 < N and next1 not in visited:
        visited.add(next1)
        currentQueue.append(next1)
    if next2 >= 0 and next2 < N and next2 not in visited:
        visited.add(next2)
        currentQueue.append(next2)
        
print(len(visited))
'''
구슬 찾기

입력
첫 줄은 구슬의 개수를 나타내는 정수 N(1 ≤ N ≤ 99)과 저울에 올려 본 쌍의 개수 M(1 ≤ M ≤ N(N-1)/2)이 주어진다.
그 다음 M 개의 줄은 각 줄마다 두 개의 구슬 번호가 주어지는데, 앞 번호의 구슬이 뒤 번호의 구슬보다 무겁다는 것을 뜻한다.

출력
첫 줄에 무게가 중간이 절대로 될 수 없는 구슬의 수를 출력 한다.
'''

'''
- 배열을 두개 만들어 각 구슬별로 해당 구슬보다 무거운 구슬들과 가벼운 구슬들의 모음을 만든다.
이후 각 구슬들에 대하여 그 구슬보다 무겁거나 가벼운게 (N+1)/2개 이상일 경우 무게가 중간이 될 수 없게 된다.
* Pass/1st/00:09:35
'''
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
big = [[] for _ in range(N + 1)] # big[i]는 i번 구슬(i>=1)보다 무거운 구슬들의 번호들 (트리 형식으로 계속 타고갈 수 있다)
small = [[] for _ in range(N + 1)] # small[i]는 i번 구슬(i>=1)보다 가벼운 구슬들의 번호들

for i in range(M):
    bigNum, smallNum = map(int, sys.stdin.readline().rstrip().split())
    big[smallNum].append(bigNum)
    small[bigNum].append(smallNum)
    
answer = 0
for i in range(1, N + 1):
    allBigNum = set(big[i]) # i번 구슬보다 무거운 구슬들(visited의 역할도 겸한다)
    tempQueue = deque(big[i])
    
    while tempQueue: # bfs로 i번 구슬보다 무거운 구슬들을 전부 탐색
        temp = tempQueue.popleft()
        for e in big[temp]:
            if e not in allBigNum:
                allBigNum.add(e)
                tempQueue.append(e)
                
    if len(allBigNum) >= (N + 1) // 2:
        answer += 1
        continue
    
    allSmallNum = set(small[i]) # i번 구슬보다 가벼운 구슬들(visited의 역할도 겸한다)
    tempQueue = deque(small[i])
    
    while tempQueue: # bfs로 i번 구슬보다 가벼운 구슬들을 전부 탐색
        temp = tempQueue.popleft()
        for e in small[temp]:
            if e not in allSmallNum:
                allSmallNum.add(e)
                tempQueue.append(e)
                
    if len(allSmallNum) >= (N + 1) // 2:
        answer += 1
        continue
    
print(answer)
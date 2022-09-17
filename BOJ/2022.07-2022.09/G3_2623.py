'''
음악프로그램

입력
첫째 줄에는 가수의 수 N과 보조 PD의 수 M이 주어진다.
가수는 번호 1, 2,…,N 으로 표시한다.
둘째 줄부터 각 보조 PD가 정한 순서들이 한 줄에 하나씩 나온다.
각 줄의 맨 앞에는 보조 PD가 담당한 가수의 수가 나오고, 그 뒤로는 그 가수들의 순서가 나온다.
N은 1이상 1,000이하의 정수이고, M은 1이상 100이하의 정수이다.

출력
출력은 N 개의 줄로 이뤄지며, 한 줄에 하나의 번호를 출력한다.
이들은 남일이가 정한 가수들의 출연 순서를 나타낸다.
답이 여럿일 경우에는 아무거나 하나를 출력 한다.
만약 남일이가 순서를 정하는 것이 불가능할 경우에는 첫째 줄에 0을 출력한다.
'''

'''
- 각 가수번호에 대하여 출연하기 위해 먼저 나와야하는 가수들의 번호들을 조건으로 저장해놓는다.
그 후, 조건이 없는 가수부터 출연시키고 가수가 출연할 때마다 만족된 조건들을 지워나간다.
만약 더 출연시킬 수 있는 가수가 없다면 0을 출력하도록 한다.
* Pass/1st/00:18:44
'''
from collections import deque

N, M = map(int, input().split()) # N: 가수의 수, M: 보조 PD의 수

prevArr = [set() for _ in range(N+1)] # prev[i]는 i번 가수(i>=1)가 출연하기 위해 먼저 나와야하는 가수들의 번호들
nextArr = [set() for _ in range(N+1)] # next[i]는 i번 가수를 조건으로 하는 가수들의 번호들

for i in range(M):
    tempArr = list(map(int, input().split()))[1:] # 보조 PD에 대한 입력
    
    for j in range(len(tempArr)):
        if j + 1 < len(tempArr):
            nextArr[tempArr[j]].add(tempArr[j + 1])
        if j - 1 >= 0:
            prevArr[tempArr[j]].add(tempArr[j - 1])

answer = []
visited = set()
tempQueue = deque() # 큐를 만들어 조건이 더 이상 필요 없는 가수들을 여기다 넣음
for i in range(1, len(prevArr)):
    if len(prevArr[i]) == 0:
        tempQueue.append(i)
        
while tempQueue:
    temp = tempQueue.popleft()
    
    if temp in visited:
        continue
    visited.add(temp)
    answer.append(temp)
    
    for e in nextArr[temp]: # temp를 조건으로 하는 모든 가수에 대하여
        prevArr[e].discard(temp) # temp를 조건으로 지우고
        if len(prevArr[e]) == 0: # 조건이 없어질 경우 큐에 넣는다
            tempQueue.append(e)

if len(answer) == N:
    for e in answer:
        print(e)
else:
    print(0)
    
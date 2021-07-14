'''
스타트링크

입력
첫째 줄에 F, S, G, U, D가 주어진다. (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 가장 높은 층은 F층이다.

출력
첫째 줄에 강호가 S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 출력한다. 만약, 엘리베이터로 이동할 수 없을 때는 "use the stairs"를 출력한다.
'''

'''
- S층을 기준으로 버튼을 늘려가는 BFS방식을 고안해볼 수 있다.
* Fail/1st/00:36:38

- 테스트 케이스에선 문제가 없었던 것으로 보아 복잡한 경우에서 상수로 설정했던 INF를 넘어서는 경우가 있어서 그런가 싶어 INF값을 늘려보았다.
* Fail/2nd/00:43:43

- 다시보니까 프린트문 출력할 때 오타가 있었다. 다시는 이런 실수를 안하도록 조심해야 겠다.
* Pass/3rd/00:51:21
'''
from collections import deque ## 큐 이용 위함

F, S, G, U, D = map(int, input().split())
INF = 1000000000

stair = [INF] * (F+1) # stair[i]는 i층으로 갈 때 눌러야하는 최소 버튼 수
stair[S] = 0 # 시작점

stairQueue = deque() # bfs 방식 사용

if(S+U<=F):
    stairQueue.append((S+U, 1)) # (a, b)는 a층으로 가는데 버튼 b개로 갈 수 있음을 의미
if(S-D>=1):
    stairQueue.append((S-D, 1))

while(stairQueue):
    (a, b) = stairQueue.popleft()
    if(stair[a]>b): # 새로운 방식이 더 빠른 경우
        stair[a]=b
        if(a+U<=F):
            stairQueue.append((a+U, b+1)) # 새로운 경우의 수 추가
        if(a-D>=1):
            stairQueue.append((a-D, b+1))

if(stair[G]==INF):
    print("use the stairs")
else:
    print(stair[G])
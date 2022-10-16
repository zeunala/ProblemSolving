'''
욕심쟁이 판다

입력
첫째 줄에 대나무 숲의 크기 n(1 ≤ n ≤ 500)이 주어진다.
그리고 둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보가 주어진다.
대나무 숲의 정보는 공백을 사이로 두고 각 지역의 대나무의 양이 정수 값으로 주어진다.
대나무의 양은 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에는 판다가 이동할 수 있는 칸의 수의 최댓값을 출력한다.
'''

'''
- 숲의 각 칸에 번호를 붙이고, 각 칸 별로 이동할 수 있는 칸 번호를 체크한다.
무조건 큰 수로 이동할 수 있는 특성상 방문했던 자리로 이동할 수가 없으므로 visited 체크 없이 BFS를 이용한다.
* Fail/1st/00:17:52
- 큐가 너무 커지는 것을 막기 위해 visited와 유사하게 각 칸별로 현재까지의 최대 칸수를 저장한 뒤,
너 칸수를 넘어서는 경우만 저장하도록 수정하였다.
* Fail/2nd/00:22:55/TimeOver
- 반복문의 순서를 바꿔서 1번 시작점으로 하는 경로를 모두 탐색한 후 다음 시작점으로 하는 경로를 탐색하도록 수정하였다.
* Fail/3rd/00:33:34/TimeOver
- 대나무가 적은 곳부터 탐색해서 중복탐색을 최소화시키도록 한다.
* Fail/4th/00:49:40/TimeOver
- 최적화 작업을 추가하였다.
* Fail/5th/00:52:35/TimeOver
- canMove 목록에서 탐색할 때 대나무가 적은 곳부터 먼저 가도록 하고,
추가로 DFS로 탐색하도록 수정하였다.
* Fail/6th/00:57:33/TimeOver
- 스택대신 우선순위 큐를 사용하여 대나무가 적은 곳부터 방문하도록 수정하였다.
* Pass/7th/01:14:08
- 문제 풀이 이후 다른 사람의 풀이를 찾아본 결과 dp + dfs를 활용해서 dfs탐색하되,
이미 dp배열(앞으로 더 방문할 수 있는 개수 저장)에 결과가 있다면 그걸 사용하도록 하는 방법도 있음을 알게 되었다.
'''
import heapq

n = int(input())
arr = [] # 0번 ~ n^2-1번 까지의 값 존재
for i in range(n):
    temp = list(map(int, input().split()))
    arr.extend(temp)

canMove = [[] for _ in range(len(arr))] # canMove[i]는 i번에서 몇 번으로 이동할 수 있는지 나타냄
for i in range(n):
    for j in range(n):
        # 위로 이동할 수 있는지 체크
        if i - 1 >= 0 and arr[n * i + j] < arr[n * (i - 1) + j]:
            canMove[n * i + j].append(n * (i - 1) + j)
        
        # 아래로 이동할 수 있는지 체크
        if i + 1 < n and arr[n * i + j] < arr[n * (i + 1) + j]:
            canMove[n * i + j].append(n * (i + 1) + j)
        
        # 왼쪽으로 이동할 수 있는지 체크
        if j - 1 >= 0 and arr[n * i + j] < arr[n * i + (j - 1)]:
            canMove[n * i + j].append(n * i + (j - 1))
        
        # 오른쪽으로 이동할 수 있는지 체크
        if j + 1 < n and arr[n * i + j] < arr[n * i + (j + 1)]:
            canMove[n * i + j].append(n * i + (j + 1))
            
        # canMove를 대나무가 적은게 앞에 오도록 재배치한다.
        canMove[n + i * j].sort(key = lambda x : arr[x])
          
# 이제 BFS로 최대 몇 칸 이동할 수 있는지 체크한다.  
answer = 0
tempHeap = [] # (-현재까지 이동한 칸 수, 현재 위치한 칸)의 최소힙이며 따라서 현재 많이 이동한 곳부터 먼저 방문하게 된다.
maxStep = [1] * len(arr) # maxStep[i]은 i번칸을 도착지로 했을 때의 최대 칸수를 의미한다.

visitedOrderHeap = [] # (arr[i], i, step) 을 저장해서 대나무가 적은게 우선시되는 힙을 만든다.
for i in range(len(arr)):
    heapq.heappush(visitedOrderHeap, (arr[i], i, 1))

while visitedOrderHeap: # 대나무가 가장 적은 곳부터 탐색
    _, i, step = heapq.heappop(visitedOrderHeap)

    if maxStep[i] > step: # 이미 더 높은 step으로 방문한적 있는 경우엔 굳이 탐색 안해도 된다.
        continue
    
    if answer < step: # 현재까지 이동한 칸 수가 높다면 갱신
        answer = step
        
    for e in canMove[i]:
        if maxStep[e] < step + 1:
            maxStep[e] = step + 1
            heapq.heappush(visitedOrderHeap, (arr[i], e, step + 1))
        
print(answer)
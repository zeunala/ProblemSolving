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
'''
from collections import deque

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
          
# 이제 BFS로 최대 몇 칸 이동할 수 있는지 체크한다.  
answer = 0
tempDeque = deque() # (현재 위치한 칸, 현재까지 이동한 칸 수) 의 값을 가진다.
for i in range(len(arr)):
    tempDeque.append((i, 1))
    
while tempDeque:
    (a, b) = tempDeque.popleft()
    
    if answer < b: # 현재까지 이동한 칸 수가 높다면 갱신
        answer = b
        
    for e in canMove[a]:
        tempDeque.append((e, b + 1))
        
print(answer)
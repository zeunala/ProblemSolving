'''
투명

입력
첫째 줄에 N과 M이 주어진다. N은 0보다 크거나 같고, 50보다 작거나 같다.
M은 0보다 크거나 같고, 50보다 작거나 같다. 둘째 줄부터 N개의 줄에 종이의 좌표가 주어진다.
왼쪽 아래 모서리의 x, y좌표, 오른쪽 위 모서리의 x, y좌표 순으로 주어진다.
모든 좌표는 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 출력한다.
'''

'''
- 입력의 범위가 작으므로 반복문으로 각 칸에 숫자를 더하는 식으로 진행한다.
* Fail/1st/00:04:21
- 1부터 시작하는 좌표를 0부터 시작하는 좌표로 변경한다.
* Pass/2nd/00:07:27
'''
N, M = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]

for x in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    # 1부터 시작하는 좌표를 0부터 시작하는 좌표로 변경
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            arr[i][j] += 1
            
answer = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] > M:
            answer += 1
            
print(answer)
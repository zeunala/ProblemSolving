'''
로봇 청소기

입력
첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)
둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다.
d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다.
빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.
로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.

출력
로봇 청소기가 청소하는 칸의 개수를 출력한다.
'''

'''
- N, M 개수가 적으므로 문제의 조건을 그대로 구현만 하면 풀릴 것으로 보인다.
빈 칸은 0, 벽은 1로 주어진 것에서 청소한 곳을 2로 표시해나가고, 마지막에 2의 개수를 구하면 된다.
* Pass/1st/00:26:33
'''
def cleanMap(arr, r, c, d):
    leftDirection = [3, 0, 1, 2] # leftDirection[d]는 d에서 왼쪽방향으로 돌린 결과를 나타낸다. (ex. d가 북쪽이면 leftDirection[d]는 서쪽)

    arr[r][c] = 2 # 현재위치 청소

    # 왼쪽 방향에 청소하지 않은 공간 존재시 한 칸 전진후 처음부터 진행, 없다면 회전 후 다시 탐색
    for i in range(4):
        d = leftDirection[d] # 왼쪽으로 회전
        if d == 0 and arr[r-1][c] == 0:
            return cleanMap(arr, r-1, c, d)
        elif d == 1 and arr[r][c+1] == 0:
            return cleanMap(arr, r, c+1, d)
        elif d == 2 and arr[r+1][c] == 0:
            return cleanMap(arr, r+1, c, d)
        elif d == 3 and arr[r][c-1] == 0:
            return cleanMap(arr, r, c-1, d)
    
    # 네 방향 모두 청소되어 있거나 벽인 경우 한 칸 후진 후 다시 탐색
    if d == 0 and arr[r+1][c] != 1:
        return cleanMap(arr, r+1, c, d)
    elif d == 1 and arr[r][c-1] != 1:
        return cleanMap(arr, r, c-1, d)
    elif d == 2 and arr[r-1][c] != 1:
        return cleanMap(arr, r-1, c, d)
    elif d == 3 and arr[r][c+1] != 1:
        return cleanMap(arr, r, c+1, d)

    # 후진도 못하면 작동정지
    return



N, M = map(int, input().split()) # N: 세로 크기, M: 가로 크기
r, c, d = map(int, input().split()) # 로봇청소기가 (r,c)에 존재, 방향은 d
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

cleanMap(arr, r, c, d)

answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            answer += 1

print(answer)

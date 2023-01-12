'''
컴백홈

입력
첫 줄에 정수 R(1 ≤ R ≤ 5), C(1 ≤ C ≤ 5), K(1 ≤ K ≤ R×C)가 공백으로 구분되어 주어진다.
두 번째부터 R+1번째 줄까지는 R×C 맵의 정보를 나타내는 '.'과 'T'로 구성된 길이가 C인 문자열이 주어진다.

출력
첫 줄에 거리가 K인 가짓수를 출력한다.
'''

'''
- BFS방식으로 모든 경우를 탐사하되, 방문한 점을 나타내는 visited 배열을 전역으로 두지 말고 각 경로마다 두도록 한다.
* Pass/1st/00:21:59
- 문제 풀이 이후 다른 사람의 풀이를 본 결과 DFS로 풀이하는 것이 현재 경로를 매번 저장할 필요가 없기에 더 효율적일 것으로 보인다.
'''
from collections import deque

def isValidPosition(pos, R, C): # 위치 정보가 R행 C열 범위 안의 유효한 좌표값인지 여부 리턴
    if pos[0] < 0 or pos[0] >= R:
        return False
    if pos[1] < 0 or pos[1] >= C:
        return False
    return True

R, C, K = map(int, input().split()) # R행 C열의 맵중 거리가 K인 경로의 가짓수를 출력해야함
arr = [] # 풀이 편의상 왼쪽 아래~오른쪽 위로 가는 것이 아니라 왼쪽 위~오른쪽 아래로 가도록 한다.

for i in range(R):
    arr.insert(0, list(input())) # 첫행을 마지막행에 오도록 해서 위와 아래를 반전시킨다.
    
tempDeque = deque() # 각 원소들은 현재까지 방문한 점들의 배열을 가지고 있다.
tempDeque.append([(0, 0)])

answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while tempDeque:
    next = tempDeque.popleft() # next는 현재까지 방문한 점들의 배열
    currentPosition = next[-1] # 현재 위치는 배열의 마지막 원소
    
    if len(next) == K:
        if currentPosition[0] == R - 1 and currentPosition[1] == C - 1:
            answer += 1
        else:
            continue
    
    for i in range(len(dx)):
        nextPosition = (currentPosition[0] + dx[i], currentPosition[1] + dy[i])
        if isValidPosition(nextPosition, R, C) and arr[nextPosition[0]][nextPosition[1]] != "T" and nextPosition not in next:
            tempDeque.append(next + [nextPosition])
            
print(answer)
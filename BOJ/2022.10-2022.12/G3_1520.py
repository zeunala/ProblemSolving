'''
내리막 길

입력
첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다.
이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다.
M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.

출력
첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.
'''

'''
- 지점의 개수가 250000개라서 시간초과가 나지 않도록 최적화가 필요하다.
무조건 높이가 낮은 곳으로만 갈 수 있으므로, 우선순위큐를 이용해 높이가 높은 곳부터 상하좌우를 탐색해본다.
* Pass/1st/00:26:58
'''
import sys
import heapq


M, N = map(int, sys.stdin.readline().rstrip().split()) # M: 세로, N: 가로
arr = [] # 지점의 높이
caseNumArr = [[0 for _ in range(N)] for _ in range(M)] # 해당 지점으로 갈 수 있는 경우의 수
tempHeap = [] # 우선순위 큐, 높이가 높은 곳이 우선적으로 담김
visited = set() # 방문한 지점들이 담김

for i in range(M):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 초기화    
heapq.heappush(tempHeap, (-arr[0][0], 0, 0)) # 우선순위 큐에는 (-높이, 세로좌표, 가로좌표)가 담김
caseNumArr[0][0] = 1

answer = 0
while tempHeap:
    val, iPos, jPos = heapq.heappop(tempHeap)
    val *= -1
    
    if (iPos, jPos) in visited:
        continue
    else:
        visited.add((iPos, jPos))
    
    if iPos == M - 1 and jPos == N - 1: # 목적지에 도달시 경우의 수 출력하고 종료
        answer = caseNumArr[iPos][jPos]
        break
    
    for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= iPos + di and iPos + di < M and 0 <= jPos + dj and jPos + dj < N and val > arr[iPos + di][jPos + dj]:
            caseNumArr[iPos + di][jPos + dj] += caseNumArr[iPos][jPos]
            heapq.heappush(tempHeap, (-arr[iPos + di][jPos + dj], iPos + di, jPos + dj))
            
print(answer)
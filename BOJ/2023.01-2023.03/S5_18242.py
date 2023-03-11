'''
네모네모 시력검사

입력
첫 번째 줄에 직사각형의 높이 N과 너비 M이 주어진다. (5 ≤ N, M ≤ 100)
두 번째 줄부터 N개의 줄에 길이가 M인 문자열이 주어진다.
i+1번째 줄의 j번째 문자가 ‘ # ’ 일 경우 색칠한 칸, ‘ . ’ 일 경우 색칠하지 않은 칸을 나타낸다.
문제에서 제시한 조건에 맞는 입력만 주어진다.

출력
정사각형의 색칠하지 않은 한 변이 왼쪽, 오른쪽, 위쪽, 아래쪽일 때에 따라 각각 LEFT, RIGHT, UP, DOWN을 출력한다.
'''

'''
- 우선 정사각형의 왼쪽위와 오른쪽아래 끝의 좌표를 계산해본다.
예를 들어 (2, 2), (6, 6)에 있다면 정사각형의 중심은 (4, 4)이며,
(2, 4), (4, 2), (6, 4), (4, 6) 중 어느 곳이 비었는지 확인하면 된다.
* Pass/1st/00:11:31
'''
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = []
for i in range(N):
    arr.append(list(sys.stdin.readline().rstrip()))

leftUp = None # 왼쪽위 끝점의 위치
rightDown = None # 오른쪽 아래 끝점의 위치

for i in range(N):
    if leftUp != None:
        break
    for j in range(M):
        if arr[i][j] == "#":
            leftUp = (i, j)
            break

for i in range(N - 1, -1, -1):
    if rightDown != None:
        break
    for j in range(M - 1, -1, -1):
        if arr[i][j] == "#":
            rightDown = (i, j)
            break

# 중심의 위치
mid = ((leftUp[0] + rightDown[0]) // 2, (leftUp[1] + rightDown[1]) // 2)

if arr[leftUp[0]][mid[1]] == ".":
    print("UP")
elif arr[mid[0]][leftUp[1]] == ".":
    print("LEFT")
elif arr[mid[0]][rightDown[1]] == ".":
    print("RIGHT")
elif arr[rightDown[0]][mid[1]] == ".":
    print("DOWN")
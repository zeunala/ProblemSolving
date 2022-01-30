'''
구슬 탈출 2

입력
첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다.
다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다.
이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다.
'.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다.
'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.
입력되는 모든 보드의 가장자리에는 모두 '#'이 있다.
구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

출력
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다.
만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.
'''

'''
- 각 방향에 따라 구슬이 움직인 결과를 리턴하는 함수를 정의하고, DFS로 탐색해본다.
이 때, 한 번의 행동에서 빨간 구슬이 움직이지 않을 경우 가지치기를 통해 탐색 횟수를 줄이도록 한다.
* Fail/1st/00:49:34
'''
import sys
from copy import deepcopy

sys.setrecursionlimit(10000)

minRotate = 11 # 최소 몇 번 돌려야 하는지

# 구슬을 이동시켜 (Rpos, Bpos, result)의 결과를 리턴한다. result는 구슬이 빠졌다면 빠진 구슬에 따라 "R" 또는 "B"가 된다. (B 우선)
def nextField(field, direction, Rpos, Bpos, Opos): # direction: 0(상), 1(하), 2(좌), 3(우)
    # 구슬이 어느쪽으로 움직이는지
    nextStep = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nextRow = nextStep[direction][0]
    nextCol = nextStep[direction][1]
    result = None
    
    # R구슬을 끝까지 이동시킨다.
    while True:
        if field[Rpos[0]+nextRow][Rpos[1]+nextCol] != "#" and (Rpos[0]+nextRow, Rpos[1]+nextCol) != Bpos:
            Rpos = (Rpos[0]+nextRow, Rpos[1]+nextCol)
            if Rpos == Opos and result == None:
                result = "R"
                Rpos = (-1, -1) # B구슬과 겹치지 않게 치워놓음
                break
        else:
            break
    # B구슬을 끝까지 이동시킨다.
    while True:
        if field[Bpos[0]+nextRow][Bpos[1]+nextCol] != "#" and (Bpos[0]+nextRow, Bpos[1]+nextCol) != Rpos:
            Bpos = (Bpos[0]+nextRow, Bpos[1]+nextCol)
            if Bpos == Opos: # result에 R이 있더라도 덮어씀
                result = "B"
                break
        else:
            break
    # R구슬을 끝까지 이동시킨다. (RB... 과 같이 B에 막힌 경우 때문에 한 번 더 체크해준다)
    while result == None:
        if field[Rpos[0]+nextRow][Rpos[1]+nextCol] != "#" and (Rpos[0]+nextRow, Rpos[1]+nextCol) != Bpos:
            Rpos = (Rpos[0]+nextRow, Rpos[1]+nextCol)
            if Rpos == Opos and result == None:
                result = "R"
                break
        else:
            break
    
    return (Rpos, Bpos, result)
        
def dfs(field, N, Rpos, Bpos, Opos):
    global minRotate
    if N >= minRotate: # 현재 돌린 횟수가 최솟값을 초과했으면 더 탐색할 필요가 없다.
        return
    
    for i in range(4):
        (newRpos, newBpos, result) = nextField(field, i, Rpos, Bpos, Opos)
        
        if Rpos == newRpos: # 돌려도 R위치 그대로이면 거기서 더 나아가지 않는다.
            continue
        elif result == "B": # B가 O에 빠져도 마찬가지
            continue
        elif result == "R": # R이 O에 빠졌다면 minRotate 갱신 후 스톱
            if N < minRotate:
                minRotate = N
            continue
        else:
            dfs(field, N+1, newRpos, newBpos, Opos)
    
    

N, M = map(int, input().split()) # N행 M열
field = []
for i in range(N):
    field.append(list(input()))

Rpos = (0, 0) # R의 위치
Bpos = (0, 0) # B의 위치
Opos = (0, 0) # O의 위치
for i in range(N):
    for j in range(M):
        if field[i][j] == "R":
            Rpos = (i, j)
            field[i][j] = "."
        if field[i][j] == "B":
            Bpos = (i, j)
            field[i][j] = "."
        if field[i][j] == "O":
            Opos = (i, j)
            
dfs(field, 1, Rpos, Bpos, Opos)
if minRotate == 11: # 갱신이 안되었을 경우
    minRotate = -1 # 결과는 -1
print(minRotate)

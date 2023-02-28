'''
나이트 투어

입력
36개의 줄에 나이트가 방문한 순서대로 입력이 주어진다.
체스판에 존재하는 칸만 입력으로 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.
'''

'''
- 문제의 요구사항을 그대로 구현하도록 한다.
모든 경로를 한 번씩만 방문해야하며 매 이동마다 나이트가 한 번 이동할 수 있는 만큼 이동해야 한다.
또한 마지막에 시작점으로 돌아올 수 있어야 한다.
* Pass/1st/00:16:40
'''
import sys

def isValidMove(old, new): # old에서 new로 이동할 수 있는지 여부 리턴
    oldTuple = (ord(old[0]) - ord("A") + 1, int(old[1])) # A1을 (1, 1) 꼴로 바꿈
    newTuple = (ord(new[0]) - ord("A") + 1, int(new[1]))
    
    # 가능한 나이트의 이동
    possibleMove = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1)]
    
    for (dx, dy) in possibleMove:
        if (oldTuple[0] + dx, oldTuple[1] + dy) == newTuple:
            return True
    return False
    

TOTAL_STEP = 36
visited = []

answer = True

for i in range(TOTAL_STEP):
    step = sys.stdin.readline().rstrip()
    visited.append(step)

if len(set(visited)) != TOTAL_STEP: # 모든 경로를 한 번씩만 방문하는 지 확인
    answer = False
if answer: # 모든 이동이 유효한지 확인
    for i in range(len(visited) - 1):
        if isValidMove(visited[i], visited[i + 1]) == False:
            answer = False
            break
if answer: # 마지막에 시작점으로 돌아올 수 있는지 확인
    if isValidMove(visited[-1], visited[0]) == False:
        answer = False
    
if answer:
    print("Valid")
else:
    print("Invalid")
            
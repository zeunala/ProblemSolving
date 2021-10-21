'''
톱니바퀴

입력
첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태가 주어진다.
상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.
다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다.
각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다.
방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

출력
총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.
1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
'''

'''
- 톱니바퀴의 개수와 회전 횟수가 적으므로 문제 요구사항 그대로 구현만 하면 되는 것으로 보인다.
* Pass/1st/00:26:37
- 문제를 풀고 다른 풀이를 찾아보니 deque의 rotate함수를 이용하면 turnRing함수 정의할 필요없이 간편하게 풀 수 있다는 것을 알게 되었다.
또한 문제에서는 톱니바퀴 개수가 적어서 하드코딩으로 구현했지만 톱니바퀴 개수가 많아진다면
해당 톱니바퀴 기준 왼쪽과 오른쪽을 각각 반복문을 돌려 톱니바퀴별로 회전방향들을 다 지정해놓았다가 한 번에 돌리는 식의 다른 풀이가 더 좋을 것이다.
'''
from queue import deque

def turnRing(ring, turnDir): # turnDir이 1이면 시계방향, -1이면 반시계 방향으로 돌림
    if turnDir == 1:
        temp = ring.pop()
        ring.appendleft(temp)
    elif turnDir == -1:
        temp = ring.popleft()
        ring.append(temp)


ring1 = deque(list(map(int, list(input()))))
ring2 = deque(list(map(int, list(input()))))
ring3 = deque(list(map(int, list(input()))))
ring4 = deque(list(map(int, list(input()))))

K = int(input())
turnList = []
for i in range(K):
    turnList.append(list(map(int, input().split())))

# 입력에 따라 톱니바퀴를 돌림
for i in range(K):
    ringNo = turnList[i][0]
    turnDir = turnList[i][1]

    # 회전 직전의 기준으로 움직이므로 모든 조건 체크 후에 톱니바퀴가 움직이도록 한다.
    if ringNo == 1:
        if ring1[2] != ring2[6]:
            if ring2[2] != ring3[6]:
                if ring3[2] != ring4[6]:
                    turnRing(ring4, -turnDir)
                turnRing(ring3, turnDir)
            turnRing(ring2, -turnDir)
        turnRing(ring1, turnDir)

    elif ringNo == 2:
        if ring1[2] != ring2[6]:
            turnRing(ring1, -turnDir)
        if ring2[2] != ring3[6]:
            if ring3[2] != ring4[6]:
                turnRing(ring4, turnDir)
            turnRing(ring3, -turnDir)
        turnRing(ring2, turnDir)

    elif ringNo == 3:
        if ring3[2] != ring4[6]:
            turnRing(ring4, -turnDir)
        if ring2[2] != ring3[6]:
            if ring1[2] != ring2[6]:
                turnRing(ring1, turnDir)
            turnRing(ring2, -turnDir)
        turnRing(ring3, turnDir)

    elif ringNo == 4: 
        if ring3[2] != ring4[6]:
            if ring2[2] != ring3[6]:
                if ring1[2] != ring2[6]:
                    turnRing(ring1, -turnDir)
                turnRing(ring2, turnDir)
            turnRing(ring3, -turnDir)
        turnRing(ring4, turnDir)

result = 0
if ring1[0] == 1:
    result += 1
if ring2[0] == 1:
    result += 2
if ring3[0] == 1:
    result += 4
if ring4[0] == 1:
    result += 8

print(result)
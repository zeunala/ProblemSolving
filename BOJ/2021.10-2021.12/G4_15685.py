'''
드래곤 커브

입력
첫째 줄에 드래곤 커브의 개수 N(1 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에는 드래곤 커브의 정보가 주어진다.
드래곤 커브의 정보는 네 정수 x, y, d, g로 이루어져 있다.
x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다. (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)
입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다. 드래곤 커브는 서로 겹칠 수 있다.
방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다.
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)

출력
첫째 줄에 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력한다.
'''

'''
- 드래곤커브를 그리는 것이 핵심으로 보인다. 꼭짓점만 제대로 잡으면 문제에서 요구한 답을 구할 수 있으므로,
시작점과 끝점만 잘 알아두었다가 모든 점에 대해서 각각 끝점에 대해 시계방향 90도 회전시키고, 이 때 시작점을 이동시킨게 새로운 끝점이 된다.
우선 A점에 대해 B점을 시계방향으로 90도 회전 시켰을 때의 좌표를 출력하는 함수를 만들고, 이를 반복호출시키자.
* Fail/1st/01:02:39/IndexError
- 그리는 도중에 IndexError가 나는 경우로 보이는데 일단 좌표들을 배열로 옮길 때 범위를 지정해보자.
* Fail/2nd/01:04:22
- x,y범위가 0이상 100이하라서 총 격자가 100*100이 아니라 101*101이다. 처음에 IndexError 난 것도 배열을 [100][100]까지만 만들어서 난 것으로 추측된다.
* Pass/3rd/01:13:05
- 문제를 풀고 다른 사람의 풀이를 찾아보니 규칙을 발견해서 푸는 방법도 있음을 알게 되었다.
방향을 입력에서의 조건처럼 숫자로 지정한다고 했을 때 0 -> 0 1 -> 0 1 2 1 -> 0 1 2 1 2 3 2 1 과 같이
이전 세대의 방향 정보를 뒤집고 거기에 1을 더한 값을 추가해주면 되는 것이다(4에 1더한 경우는 0으로 계산)
앞으로 이러한 형식의 문제가 나올 때 규칙성같은 것이 혹시 없을지 먼저 찾아보고 접근해야겠다.
'''
def turn90(origin, target): # origin 변수 기준으로 target을 시계방향으로 90도 돌린 좌표 리턴
    temp = (target[0] - origin[0], target[1] - origin[1]) # origin만큼 빼서 원점에 대해 시계방향 90도 돌리고 다시 더할 것임
    # 배열이 y값이 커질수록 아래로 가는 구조라 일반좌표계에서 시계반대방향으로 90도 돌려야 배열에서 시계방향 90도의 효과를 낸다.
    tempTurn = (-temp[1], temp[0]) # (x, y) -> (-y, x)
    result = (tempTurn[0] + origin[0], tempTurn[1] + origin[1])
    return result

def drawDragon(x, y, d, g): # 드래곤 커브 정보가 주어지면 꼭짓점들을 1로, 나머지를 0으로 표시한 101*101 배열 리턴 
    start = (x, y)
    end = (0, 0)

    if d == 0:
        end = (x + 1, y)
    elif d == 1:
        end = (x, y - 1)
    elif d == 2:
        end = (x - 1, y)
    elif d == 3:
        end = (x, y + 1)
    
    allPoint = [start, end] # 현재 그려진 커브의 꼭짓점들

    for i in range(g): # 앞으로 g세대 더 그리면 된다
        newAllPoint = allPoint[:]
        newEnd = (0, 0)

        while allPoint:
            e = allPoint.pop()
            newE = turn90(end, e)
            newAllPoint.append(newE)

            if e[0] == start[0] and e[1] == start[1]: # 처음 start를 꺼낸 거였으면 그걸 돌린게 newEnd가 된다.
                newEnd = newE

        allPoint = newAllPoint[:]
        end = newEnd

    resultArr = [[0 for _ in range(101)] for _ in range(101)] # 여기에 allPoint의 점들을 다 1로 표시할 것임
    while allPoint:
        e = allPoint.pop()
        resultArr[e[1]][e[0]] = 1

    return resultArr

N = int(input()) # 드래곤 커브의 개수
field = [[0 for _ in range(101)] for _ in range(101)]
for i in range(N):
    x, y, d, g = map(int, input().split())
    extraField = drawDragon(x, y, d, g)
    for i2 in range(101):
        for j2 in range(101):
            field[i2][j2] += extraField[i2][j2]
    
answer = 0
for i in range(100):
    for j in range(100):
        if field[i][j] * field[i][j+1] * field[i+1][j] * field[i+1][j+1] > 0:
            answer += 1

print(answer)
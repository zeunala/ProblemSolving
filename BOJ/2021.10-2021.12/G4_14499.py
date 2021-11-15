'''
주사위 굴리기
입력
첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20),
주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1),
그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.
둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다.
주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.
마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.

출력
이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
'''

'''
- 문제에 적힌 그대로 구현만 하면 되는 문제로 보인다. 주사위 방향만 헷갈리지 않도록 조심하자.
* Pass/1st/00:39:17
'''
def diceRoll(currentDice, direction): # currentDice 상태에서 어떤 방향으로 굴렸을 때 바뀌는 currentDice 결과 리턴
    (main, right, up) = currentDice
    if direction == 1: # 동쪽으로 움직일 경우
        return (right, 7-main, up)
    if direction == 2: # 서쪽으로 움직일 경우
        return (7-right, main, up)
    if direction == 3: # 북쪽으로 움직일 경우
        return (up, right, 7-main)
    if direction == 4: # 남쪽으로 움직일 경우
        return (7-up, right, main)

N, M, x, y, K = map(int, input().split())
mapArr = []
for i in range(N):
    mapArr.append(list(map(int, input().split())))
comArr = list(map(int, input().split()))

diceNum = [0, 0, 0, 0, 0, 0, 0] # 주사위에 적힌 눈금(0번 원소는 쓰이지 않는다)

# 주사위 면을 1~6번까지 붙인다고 했을 때 첫번째 원소는 바닥에 있는 면의 번호, 두번째 원소는 동쪽 면의 번호, 세번째 원소는 북쪽 면의 번호
# 한 면이 n이면 반대 편에 있는 면은 7-n이다.
currentDice = (6, 3, 2)
currentPos = (x, y)

for i in range(K):
    (a, b) = currentPos
    if comArr[i] == 1: # 동쪽
        if b + 1 >= M: # 경계를 넘으려 할 경우 명령무시
            continue
        currentPos = (a, b + 1)
    elif comArr[i] == 2: # 서쪽
        if b - 1 < 0:
            continue
        currentPos = (a, b - 1)
    elif comArr[i] == 3: # 북쪽
        if a - 1 < 0:
            continue
        currentPos = (a - 1, b)
    elif comArr[i] == 4: # 남쪽
        if a + 1 >= N:
            continue
        currentPos = (a + 1, b)
    
    currentDice = diceRoll(currentDice, comArr[i])
        
    print(diceNum[7 - currentDice[0]]) # 이동시마다 윗면 출력
    if mapArr[currentPos[0]][currentPos[1]] == 0: # 이동한 곳이 0이면 바닥면의 눈금을 이동한 곳에 복사
        mapArr[currentPos[0]][currentPos[1]] = diceNum[currentDice[0]]
    else: # 아니면 도착지점의 눈금을 바닥면에 복사, 도착지점의 눈금은 0이 됨
        diceNum[currentDice[0]] = mapArr[currentPos[0]][currentPos[1]]
        mapArr[currentPos[0]][currentPos[1]] = 0
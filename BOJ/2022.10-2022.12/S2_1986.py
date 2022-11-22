'''
체스

입력
첫째 줄에는 체스 판의 크기 n과 m이 주어진다. (1 ≤ n, m ≤ 1000)
그리고 둘째 줄에는 Queen의 개수와 그 개수만큼의 Queen의 위치가 입력된다.
그리고 마찬가지로 셋째 줄에는 Knight의 개수와 위치, 넷째 줄에는 Pawn의 개수와 위치가 입력된다.
즉 둘째 줄, 셋째 줄, 넷째 줄은  k, r1, c1, r2, c2, ..., rk, ck 이 빈 칸을 사이에 두고 주어진다는 것이다
여기서 ri는 i번째 말의 행 위치, ci는 i번째 말의 열 위치를 의미한다. 한 칸에는 하나의 말만 놓인다고 가정한다.
Knight, Queen, Pawn의 개수는 각각 100을 넘지 않는 음이 아닌 정수이다.

출력
첫째 줄에 n×m 체스판에 안전한 칸이 몇 칸인지 출력하시오.
'''

'''
- 말의 개수가 많지 않으므로 하나하나 구현해본다.
* Fail/1st/00:22:14
'''
n, m = map(int, input().split())
queenArr = list(map(int, input().split()))[1:]
knightArr = list(map(int, input().split()))[1:]
pawnArr = list(map(int, input().split()))[1:]

posSet = set() # 장애물이 있는 모든 곳
isDanger = set() # 장애물은 없지만 잡아먹힐 위험이 있는 곳

for i in range(len(knightArr) // 2):
    posSet.add((knightArr[2 * i], knightArr[2 * i + 1]))
for i in range(len(queenArr) // 2):
    posSet.add((queenArr[2 * i], queenArr[2 * i + 1]))
for i in range(len(pawnArr) // 2):
    posSet.add((pawnArr[2 * i], pawnArr[2 * i + 1]))

for i in range(len(knightArr) // 2):
    x, y = knightArr[2 * i], knightArr[2 * i + 1]
    print(x, y)
    for (dx, dy) in [(-2, -1), (-1, -2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, 2), (-2, 1)]:
        if x + dx >= 1 and x + dx <= n and y + dy >= 1 and y + dy <= m and (x + dx, y + dy) not in posSet:
            isDanger.add((x + dx, y + dy))
for i in range(len(queenArr) // 2):
    x, y = queenArr[2 * i], queenArr[2 * i + 1]
    for (dx, dy) in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        count = 1
        while x + count * dx >= 1 and x + count * dx <= n and y + count * dy >= 1 and y + count * dy <= m and (x + count * dx, y + count * dy) not in posSet:
            isDanger.add((x + count * dx, y + count * dy))
            count += 1
    
answer = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i, j) not in posSet and (i, j) not in isDanger:
            answer += 1
            
print(answer)
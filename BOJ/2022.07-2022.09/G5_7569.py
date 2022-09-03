'''
토마토

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다.
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다.
둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다.
즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다.
각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
이러한 N개의 줄이 H번 반복하여 주어진다.
토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다.
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''

'''
- 문제의 요구사항을 그대로 구현하면 되는 문제로 보인다.
* Pass/1st/00:18:13
'''
M, N, H = map(int, input().split()) # 각각 가로, 세로, 높이
arr = [] # arr[a][b][c]는 a번째 상자의 b행 c열을 의미한다.
answer = 0
goodTomatoPos = set() # 익은 토마토의 위치 (a, b, c)들의 쌍 모임
badTomatoPos = set() # 익지 않은 토마토의 위치 (a, b, c)들의 쌍 모임

for i in range(H):
    tempArr = []
    for j in range(N):
        tempArr.append(list(map(int, input().split())))
    arr.append(tempArr)
    
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                goodTomatoPos.add((i, j, k))
            elif arr[i][j][k] == 0:
                badTomatoPos.add((i, j, k))
             
while badTomatoPos: # 익지 않은 토마토가 없어질 때까지 반복
    answer += 1
    badTomatoNum = len(badTomatoPos) # 익지 않은 토마토 수 저장해놨다가 1회 반복 후에도 변하지 않으면 더이상 진행불가 상황임
    tempGoodTomatoPos = set(goodTomatoPos)
    
    for e in tempGoodTomatoPos:
        goodTomatoPos.remove(e) # 한 번 체크한 것은 더 이상 체크할 필요 없으므로 익은 토마토 목록에서 제거
        (a, b, c) = e
        
        for f in [(a, b, c + 1), (a, b, c - 1), (a, b + 1, c), (a, b - 1, c), (a + 1, b, c), (a - 1, b, c)]:
            if f in badTomatoPos:
                badTomatoPos.remove(f)
                goodTomatoPos.add(f)
                
    if len(badTomatoPos) == badTomatoNum:
        answer = -1
        break

print(answer)
            
'''
도로의 개수

입력
첫째 줄에 도로의 가로 크기 N과 세로 크기 M이 주어진다.
N과 M은 100보다 작거나 같은 자연수이고, 둘째 줄에는 공사중인 도로의 개수 K가 주어진다.
K는 0보다 크거나 같고, 50보다 작거나 같은 자연수이다.
셋째 줄부터 K개 줄에는 공사중인 도로의 정보가 a b c d와 같이 주어진다.
a와 c는 0보다 크거나 같고, N보다 작거나 같은 자연수이고, b와 d는 0보다 크거나 같고, M보다 작거나 같은 자연수이다.
그리고, (a, b)와 (c, d)의 거리는 항상 1이다.

출력
첫째 줄에 (0, 0)에서 (N, M)까지 가는 경우의 수를 출력한다. 이 값은 0보다 크거나 같고, 2^63-1보다 작거나 같은 자연수이다.
'''

'''
- (0, 0)에서 (N, M)까지 가는 경우의 수는 (0, 0) ~ (N - 1, M) 경우의 수[1] + (0, 0) ~ (N, M - 1) 경우의 수[2]이다.
단, [1]의 경우 (N - 1, M) ~ (N, M)이 공사 중인 경우 제외되며,
[2]의 경우 (N, M - 1) ~ (N, M)이 공사 중인 경우 제외된다.
* Pass/1st/00:15:02
'''
N, M = map(int, input().split())
K = int(input())
bannedPos = set() # (a, b, c, d)와 같은 튜플의 형태로 구성되며, (a, b) ~ (c, d)를 이용할 수 없음을 의미
for i in range(K):
    a, b, c, d = map(int, input().split())
    bannedPos.add((a, b, c, d))
    bannedPos.add((c, d, a, b))
    
caseArr = [[0 for _ in range(M + 1)] for _ in range(N + 1)] # caseArr[i][j]는 (0, 0) ~ (i, j)까지 가는 경우의 수
caseArr[0][0] = 1

for i in range(N + 1):
    for j in range(M + 1):
        if i == 0 and j == 0:
            continue
        
        # (0, 0) ~ (N, M) = (0, 0) ~ (N - 1, M) + (0, 0) ~ (N, M - 1)
        # 첫 번째 값을 firstCase, 두 번째 값을 secondCase로 둠
        firstCase = 0
        secondCase = 0
        if i > 0 and (i - 1, j, i, j) not in bannedPos:
            firstCase = caseArr[i - 1][j]
        if j > 0 and (i, j - 1, i, j) not in bannedPos:
            secondCase = caseArr[i][j - 1]
        caseArr[i][j] = firstCase + secondCase
        
print(caseArr[-1][-1])
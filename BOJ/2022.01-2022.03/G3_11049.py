'''
행렬 곱셈 순서

입력
첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.
둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)
항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

출력
첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다.
정답은 2^31-1 보다 작거나 같은 자연수이다. 또한, 최악의 순서로 연산해도 연산 횟수가 2^31-1보다 작거나 같다.
'''

'''
- DP로 풀어보자. N*N DP배열을 만들어 dp[a][b]는 a번 행렬부터 b번 행렬까지 곱했을 때 필요한 연산 횟수를 저장하도록 한다. (a<b)
* Fail/1st/00:40:44
- k의 범위가 잘못된것 같아 수정하였다.
* Fail/2nd/00:52:59
'''
N = int(input())
matrix = []
for i in range(N):
    a, b = map(int, input().split())
    matrix.append((a, b))
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        dp[i][j] = dp[i][j-1] + matrix[i][0] * matrix[j][0] * matrix[j][1] # 우선 하나하나 다 곱하는 경우를 기준으로 삼음
    
for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        # 기존 dp[i][j]보다 중간에 걸친 값이 더 작다면 갱신
        for k in range(i+1, j):
            temp = dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            if dp[i][j] > temp:
                dp[i][j] = temp
                
print(dp[0][N-1])
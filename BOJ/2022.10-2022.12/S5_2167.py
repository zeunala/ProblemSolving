'''
2차원 배열의 합

입력
첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다.
다음 N개의 줄에는 M개의 정수로 배열이 주어진다.
배열에 포함되어 있는 수는 절댓값이 10,000보다 작거나 같은 정수이다.
그 다음 줄에는 합을 구할 부분의 개수 K(1 ≤ K ≤ 10,000)가 주어진다.
다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다(1 ≤ i ≤ x ≤ N, 1 ≤ j ≤ y ≤ M).

출력
K개의 줄에 순서대로 배열의 합을 출력한다. 배열의 합은 2^31-1보다 작거나 같다.
'''

'''
- 이차원 배열의 부분합을 구해서 계산하도록 한다.
* Fail/1st/00:29:33
- 잘못 작성한 print문을 삭제하였다.
* Pass/2nd/00:30:04
'''
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(temp)
    
arrSum = [[0 for _ in range(M)] for _ in range(N)]

# 배열의 부분합을 구함
for i in range(N):
    arrSum[i][0] = arr[i][0]
    for j in range(1, M):
        arrSum[i][j] = arrSum[i][j - 1] + arr[i][j]
    
    if i >= 1:
        for j in range(M):
            arrSum[i][j] += arrSum[i - 1][j]
            
# 1열 1행부터 시작하도록 바꿈
arrSum.insert(0, [0] * (M + 1))
for i in range(1, N + 1):
    arrSum[i].insert(0, 0)
        
K = int(sys.stdin.readline().rstrip())
for i in range(K):
    i, j, x, y = map(int, sys.stdin.readline().rstrip().split())
    print(arrSum[x][y] - arrSum[x][j - 1] - arrSum[i - 1][y] + arrSum[i - 1][j - 1])
'''
사탕 줍기 대회

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 M과 N이 주어졌다. (1 ≤ M × N ≤ 10^5) 다음 M개 줄에는 박스에 들어있는 사탕의 개수 N개가 주어진다.
박스에 들어있는 사탕은 적어도 1개이며 10^3개를 넘지 않는다.
입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해 상근이가 집을 수 있는 사탕의 최대 개수를 출력한다.
'''

'''
- 우선 각 행에 대해서 가능한 최대 사탕 개수를 구한다. (연속 사탕 집기 불가)
이후 행별로 사탕 개수를 하나로 축소시킬 수 있고, 서로 다른 행 중 연속해서 집지 않고 가질 수 있는 최대 사탕 개수를 구하는 문제로 바뀌게 된다. 
* Pass/1st/00:13:52
'''
import sys

def calcMaxCandy(arr): # 연속해서 집지 않도록 했을 때 가질 수 있는 최대 사탕 개수를 구한다.
    dp = [0] * len(arr) # dp[i]는 arr[i]까지 범위에서 가질 수 있는 최대 사탕 개수
    dp[0] = arr[0]
    
    if len(arr) >= 2:
        dp[1] = max(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
        
    return dp[-1]
        
while True:
    M, N = map(int, sys.stdin.readline().rstrip().split())
    if M == 0 and N == 0:
        break
    
    arr = []
    for i in range(M):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
        
    zipArr = [] # M*N 크기의 arr을 각 행별로 얻을 수 있는 최대 사탕값들을 구해 M크기의 배열로 만듦
    for i in range(M):
        zipArr.append(calcMaxCandy(arr[i]))
        
    print(calcMaxCandy(zipArr))
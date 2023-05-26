'''
수익

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 N이 주어져 있다. (1 ≤ N ≤ 250,000)
둘째 줄부터 N개의 줄에는 매일 매일의 수익 P가 주어진다. (-10,000 ≤ P ≤ 10,000) 수익은 첫 날부터 순서대로 주어진다.
입력의 마지막 줄에는 0이 주어진다.

출력
각 테스트 케이스에 대해서 가장 많은 수익을 올린 구간의 수익을 출력한다. 단, 구간이 비어있으면 안 된다.
'''

'''
- N의 범위가 크므로 분할정복 알고리즘을 이용한다.
A ~ B ~ C 에서의 최대 수익은 A ~ B, B ~ C, B를 사이에 둔 구간 중 한 곳에서 나온다.
* Pass/1st/00:14:34
- 문제풀이 이후 다른 풀이를 보니 dp배열을 따로 만들어서 dp[i]를 i일로 끝날 때 최대 수익으로 둬서,
max(dp)를 구하는 방식을 쓰면 더 간단하게 풀 수 있을 것으롭 보인다.
'''
import sys

INF = 10 ** 10
def getMaxPrice(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    
    # start ~ mid ~ end 중 start ~ mid 구간, mid ~ end 구간, mid를 포함한 구간 중 최댓값을 찾는다.
    case1 = -INF
    if mid > 0:
        case1 = getMaxPrice(arr[:mid])
    case2 = -INF
    if mid + 1 < len(arr):
        case2 = getMaxPrice(arr[mid + 1:])
    
    case3 = arr[mid]
    leftMax = 0 # mid를 포함하는 구간을 탐색할 때 mid 왼쪽에서의 최댓값
    rightMax = 0 # mid를 포함하는 구간을 탐색할 때 mid 오른쪽에서의 최댓값
    
    currentMax = 0
    for i in range(mid - 1, -1, -1):
        currentMax += arr[i]
        if leftMax < currentMax:
            leftMax = currentMax
    case3 += leftMax
            
    currentMax = 0
    for i in range(mid + 1, len(arr)):
        currentMax += arr[i]
        if rightMax < currentMax:
            rightMax = currentMax
    case3 += rightMax

    return max(case1, case2, case3)

while True:
    N = int(sys.stdin.readline().rstrip())
    
    if N == 0:
        break
    
    arr = []
    for i in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))
    print(getMaxPrice(arr))
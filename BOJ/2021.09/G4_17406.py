'''
배열 돌리기 4

입력
첫째 줄에 배열 A의 크기 N, M, 회전 연산의 개수 K가 주어진다.

둘째 줄부터 N개의 줄에 배열 A에 들어있는 수 A[i][j]가 주어지고, 다음 K개의 줄에 회전 연산의 정보 r, c, s가 주어진다.

출력
배열 A의 값의 최솟값을 출력한다.
'''

'''
- K의 범위가 6까지인 것으로 보아 구현문제 유형인 것으로 보인다. 조건에 맞게 잘 구현해보자.
* Pass/1st/01:02:32
'''
import sys
from itertools import permutations
from copy import deepcopy

def rollArr(arr, N, M, r, c, s): # 정해진 값에 따라 배열을 돌림
    for i in range(1, s+1): # 1칸 떨어진 곳부터 s칸 떨어진 곳까지 돌림
        # 맨 왼쪽 위부터 시계방향으로 교체해나감
        changeTarget = [] # 교체 대상들
        for j in range(c-i, c+i+1):
            changeTarget.append((r-i, j)) # 위쪽 (모서리 포함)
        for j in range(r-i+1, r+i):
            changeTarget.append((j, c+i)) # 오른쪽 (모서리 제외)
        for j in range(c+i, c-i-1, -1):
            changeTarget.append((r+i, j)) # 아래쪽 (모서리 포함)
        for j in range(r+i-1, r-i-1, -1):
            changeTarget.append((j, c-i)) # 왼쪽 (이 때 맨 왼쪽위 모서리도 중복해서 포함)

        # changeTarget[n+1]의 위치의 값을 changeTarget[n]의 위치의 값으로 교체한다.
        prevValue = arr[changeTarget[0][0]][changeTarget[0][1]]
        for j in range(1, len(changeTarget)):
            (a, b) = changeTarget[j]
            temp = arr[a][b]
            arr[a][b] = prevValue
            prevValue = temp

def evalValue(arr): # 입력으로 준 배열의 값을 리턴
    minimum = 10**9
    
    for e in arr:
        temp = sum(e)
        if minimum > temp:
            minimum = temp

    return minimum

N, M, K = map(int, sys.stdin.readline().rstrip().split())
A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))
rollOp = []
for i in range(K):
    rollOp.append(list(map(int, sys.stdin.readline().rstrip().split())))

rollOrder = list(permutations([i for i in range(K)])) # 굴릴 수 있는 모든 경우의 수

answer = 10**9
for e in rollOrder:
    tempA = deepcopy(A)
    for e2 in e:
        rollArr(tempA, N, M, rollOp[e2][0]-1, rollOp[e2][1]-1, rollOp[e2][2]) # r, c의 값은 1행1열부터 시작하는 가정하에 준 값이라 여기서 1을 빼야함
    tempValue = evalValue(tempA)
    if answer > tempValue:
        answer = tempValue

print(answer)
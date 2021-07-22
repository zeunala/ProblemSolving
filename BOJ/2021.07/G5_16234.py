'''
입력
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

출력
인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.
'''

'''
- 우선 A와 같은 크기의 배열(link)을 하나 더 만들어서 link[r][c]이 몇 번째 연합에 속하게 되는지 나타내도록 하자. 
* Fail/1st/01:23:38/Timeout
'''

import sys
import copy
from collections import deque

def countNation(link, idx): # 연합 idx에 해당하는 나라가 뭐뭐 있는지 체크
    N = len(link)
    result = []
    for i in range(N):
        for j in range(N):
            if(link[i][j]==idx):
                result.append((i,j))

    return result

def checkArrSame(A, B, n): # n*n크기의 A, B 배열이 같은지 체크
    result = True
    for i in range(n):
        for j in range(n):
            if(A[i][j]!=B[i][j]):
                result = False

    return result

N, L, R = map(int, input().split())
A = []
newA = [] # 이동이 한번 일어난 결과
link = []
answer = 0

for i in range(N):
    tempInput = list(map(int, sys.stdin.readline().rstrip().split()))
    A.append(tempInput)

while True: # 여기서 부터 한단계의 전체과정
    newA = copy.deepcopy(A) # 그냥 newA=A[:]로는 깊은 복사가 안되었다. 아마 이차원배열이라 그런듯?
    link = copy.deepcopy(A)

    for i in range(N): # link배열 -1로 초기화
        for j in range(N):
            link[i][j] = -1

    idx = 0
    for i in range(N): # 우선 연합을 결정 (BFS 이용)
        for j in range(N):
            if(link[i][j])!=-1: continue # 이미 방문한거면 idx갱신 없이 다음으로

            queue = deque([(i, j)])
            while queue:
                (m, n) = queue.popleft()

                link[m][n] = idx
                if m+1<N:
                    if abs(A[m][n]-A[m+1][n])>=L and abs(A[m][n]-A[m+1][n])<=R and link[m+1][n]!=idx: # 아래쪽 나라와 연합으로 묶일 수 있는지 확인
                        queue.append((m+1, n))
                if n+1<N:
                    if abs(A[m][n]-A[m][n+1])>=L and abs(A[m][n]-A[m][n+1])<=R and link[m][n+1]!=idx: # 오른쪽 나라와 연합으로 묶일 수 있는지 확인
                        queue.append((m, n+1))
                if m>0:
                    if abs(A[m][n]-A[m-1][n])>=L and abs(A[m][n]-A[m-1][n])<=R and link[m-1][n]!=idx: # 위쪽 나라와 연합으로 묶일 수 있는지 확인
                        queue.append((m-1, n))
                if n>0:
                    if abs(A[m][n]-A[m][n-1])>=L and abs(A[m][n]-A[m][n-1])<=R and link[m][n-1]!=idx: # 왼쪽 나라와 연합으로 묶일 수 있는지 확인
                        queue.append((m, n-1))

            idx+=1


    for i in range(idx): # 그리고 연합별로 이동
        result = countNation(link, i)
        resultLen = len(result)

        sum = 0
        for (m, n) in result: # 각 연합에 대해 합치고
            sum+=A[m][n]
        
        for (m, n) in result: # 분배
            newA[m][n]=sum//resultLen

    if checkArrSame(A, newA, N): # 변한게 없으면 루프 탈출
        break

    answer+=1
    A=copy.deepcopy(newA)

print(answer)
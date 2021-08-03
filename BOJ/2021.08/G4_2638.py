'''
치즈

입력
첫째 줄에는 모눈종이의 크기를 나타내는 두 개의 정수 N, M (5 ≤ N, M ≤ 100)이 주어진다.
그 다음 N개의 줄에는 모눈종이 위의 격자에 치즈가 있는 부분은 1로 표시되고, 치즈가 없는 부분은 0으로 표시된다.
또한, 각 0과 1은 하나의 공백으로 분리되어 있다.

출력
출력으로는 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 정수로 첫 줄에 출력한다.
'''

'''
- 구현 유형의 문제로 보인다. 각 시간마다 각각의 공간에 대해 두 면이상 접촉하는지 체크하면 되는데,
이 때 치즈 내부에 있는 공간은 외부 공기와 접촉하지 않는 것으로 가정한다는 것에 유의해야 한다.
우선 외부 공기의 칸을 -100으로 바꾼 뒤 각 치즈에 대해 상하좌우 합이 -190미만이면 녹는것으로 판정해서 구현해보기로 하였다.
* Fail/1st/00:32:19/RecursionError
- RecursionError가 떠서 테스트한 결과 범위가 커지면 checkArea함수가 너무 깊게 호출되는 것 같다. 다른 방법으로 구현해야겠다.
* Pass/2nd/00:43:27
- DFS 구현시 재귀함수가 아닌 스택을 이용하게 바꾸었더니 에러가 해결되었다. line 29-30부분의 중복 방문된 경우 생략하는 코드는 없애도 결과에 이상 없었으니 참고하자.
'''
import sys

def checkArea(arr, N, M): # 외부 공기의 칸을 -100으로 바꾸는 함수. 조건에서 맨 가장자리에는 치즈 없다고 가정했었다.
    stack = [(0,0)] # base case

    while stack:
        (i, j) = stack.pop()
        if arr[i][j]==-100: # 중복 방문된 경우 생략
            continue

        arr[i][j] = -100
        if i+1<N and arr[i+1][j]==0:
            stack.append((i+1, j))
        if j+1<M and arr[i][j+1]==0:
            stack.append((i, j+1))
        if i-1>=0 and arr[i-1][j]==0:
            stack.append((i-1, j))
        if j-1>=0 and arr[i][j-1]==0:
            stack.append((i, j-1))

def meltArea(arr, N, M): # 외부공기와 두변 이상 노출된 치즈를 녹이는 함수
    for i in range(N):
        for j in range(M):
            if arr[i][j]!=1: # 치즈가 아닌 것에는 관심없음
                continue

            sumVal = 0 # 해당 구역 네변 합산(이 값이 -190미만이라는 것은 치즈 녹는 경우에 대한 필요충분조건이다)
            if i+1<N:
                sumVal+=arr[i+1][j]
            if j+1<M:
                sumVal+=arr[i][j+1]
            if i-1>=0:
                sumVal+=arr[i-1][j]
            if j-1>=0:
                sumVal+=arr[i][j-1]

            if sumVal<-190:
                arr[i][j] = 0 # 녹아서 벽이 됨(-100으로 하지 않는 것은 치즈가 한번에 녹게 하기 위함이다)

def resetArea(arr, N, M): # -100으로 바꿨던 것을 다시 0으로 바꾸는 함수
    for i in range(N):
        for j in range(M):
            if arr[i][j]==-100:
                arr[i][j] = 0

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

t = 0 # 총 걸리는 시간
while True:
    inC = False # 치즈가 남아있는지
    for i in range(N):
        if 1 in arr[i]:
            inC = True
            break
    if not inC: # 치즈가 다 없어졌으면 종료
        break

    checkArea(arr, N, M)
    meltArea(arr, N, M)
    resetArea(arr, N, M)

    t += 1 # 시간이 흐름

print(t)
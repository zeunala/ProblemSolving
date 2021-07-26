'''
테트로미노

입력
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다.
i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 
입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
'''

'''
- 처음에는 DP나 DFS/BFS로 접근하려고 하였으나, 생각해보니 단 한 개의 케이스만 구하면 되고 총 칸 수도 250000개 밖에 되지 않는다.
테트로미노는 I, O, L, Z, T자 블록으로 나뉘는데 각각 대칭/회전을 했을 때 2, 1, 8, 4, 4개의 경우의 수가 나온다.
브루트 포스 방법을 사용해도 크게 무리가 없을 것이라 추측된다.
* Pass/1st/00:37:57
다행히 시간초과는 발생하지 않았다. 다른 사람의 풀이는 찾아보니 DFS 4회+T블록 따로 계산을 하는 방법을 쓰거나,
아니면 아래의 i+a, j+b부분의 a,b를 따로 배열로 빼는 방법을 쓰는게 더 효율적인 코드가 될 것으로 예상된다.
'''
import sys

N, M = map(int, input().split()) # N: 세로크기, M: 가로 크기
arr=[]
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split()))+[-10000, -10000, -10000]) # 경계값 조건 확인 안하도록 더미값을 넣음
for i in range(3):
    arr.append([-10000]*(M+3))

maxNum = -1

for i in range(N):
    for j in range(M):
        temp = max(arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j], arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3]) # I블록의 2가지 경우
        if(maxNum<temp):
            maxNum = temp

        temp = arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1] # O블록
        if(maxNum<temp):
            maxNum = temp
        
        temp = max(arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j+1], # L블록
        arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j], # L블록 90도 우회전
        arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1], # L블록 180도 우회전
        arr[i][j+2]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2], # L블록 270도 우회전
        arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1], # 리버스L블록 (L블록 좌우대칭)
        arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2], # 리버스L블록 90도 우회전
        arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+2][j], # 리버스L블록 180도 우회전
        arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+2]) # 리버스L블록 270도 우회전
        if(maxNum<temp):
            maxNum = temp

        temp = max(arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j+2], arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j]) # Z블록
        if(maxNum<temp):
            maxNum = temp
        temp = max(arr[i][j+1]+arr[i][j+2]+arr[i+1][j]+arr[i+1][j+1], arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j+1]) # 리버스Z블록
        if(maxNum<temp):
            maxNum = temp
        
        temp = max(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1], # T블록
        arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1], # T블록 90도 우회전
        arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2], # T블록 180도 우회전
        arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+1][j+1]) # T블록 270도 우회전
        if(maxNum<temp):
            maxNum = temp

print(maxNum)

'''
적록색약

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
'''

'''
- N이 크지 않으므로 BFS나 DFS 등을 사용하여 총 몇 개의 구역이 가능한지 하나하나 세면 될 것이다.
* Fail/1st/00:15:54/RecursionError
'''
def dfs(arr, N, i, j): # 방문한 곳을 X로 칠하며 색깔이 같은 인접한 곳들을 탐색한다.
    if arr[i][j] == "X":
        return
    
    color = arr[i][j]
    arr[i][j] = "X"
    
    if i - 1 >= 0 and arr[i - 1][j] == color:
        dfs(arr, N, i - 1, j)
    if j - 1 >= 0 and arr[i][j - 1] == color:
        dfs(arr, N, i, j - 1)
    if i + 1 < N and arr[i + 1][j] == color:
        dfs(arr, N, i + 1, j)
    if j + 1 < N and arr[i][j + 1] == color:
        dfs(arr, N, i, j + 1)
        
N = int(input())
arr = []
arrBlind = [] # 적록색약이 본 그림 (G이 R로 바뀐다)
for i in range(N):
    inputString = input()
    blindString = inputString.replace("G", "R")
    
    arr.append(list(inputString))
    arrBlind.append(list(blindString))

normalCount = 0
blindCount = 0

# 이미 방문한 노드는 X로 칠한다.
for i in range(N):
    for j in range(N):
        if arr[i][j] != "X":
            dfs(arr, N, i, j)
            normalCount += 1
        if arrBlind[i][j] != "X":
            dfs(arrBlind, N, i, j)
            blindCount += 1
            
print(str(normalCount)+ " " + str(blindCount))
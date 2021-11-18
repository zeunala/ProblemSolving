'''
알파벳

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20)
둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
'''

'''
- R과 C가 크지 않아서 모든 경우의 수를 다 체크해도 될 것으로 보인다. DFS방식으로 모두 탐색해보자.
Fail/1st/00:35:58/TimeOver
'''
from copy import deepcopy

maxValue = 0

def checkMaxValue(N): # 현재 maxValue보다 인자로 준 값이 더 클 경우 갱신
    global maxValue
    if maxValue < N:
        maxValue = N

def dfs(mapArr, R, C, pos, N, visited, alphaVisited):
    if visited[pos[0]][pos[1]] or alphaVisited[mapArr[pos[0]][pos[1]]]:
        return
    
    tempVisited = deepcopy(visited)
    tempVisited[pos[0]][pos[1]] = True
    tempAlphaVisited = deepcopy(alphaVisited)
    tempAlphaVisited[mapArr[pos[0]][pos[1]]] = True
    
    if pos[0] - 1 >= 0 and visited[pos[0] - 1][pos[1]] == False and alphaVisited[mapArr[pos[0] - 1][pos[1]]] == False:
        dfs(mapArr, R, C, (pos[0] - 1, pos[1]), N + 1, tempVisited, tempAlphaVisited)
    
    if pos[0] + 1 < R and visited[pos[0] + 1][pos[1]] == False and alphaVisited[mapArr[pos[0] + 1][pos[1]]] == False:
        dfs(mapArr, R, C, (pos[0] + 1, pos[1]), N + 1, tempVisited, tempAlphaVisited)
    
    if pos[1] - 1 >= 0 and visited[pos[0]][pos[1] - 1] == False and alphaVisited[mapArr[pos[0]][pos[1] - 1]] == False:
        dfs(mapArr, R, C, (pos[0], pos[1] - 1), N + 1, tempVisited, tempAlphaVisited)
        
    if pos[1] + 1 < C and visited[pos[0]][pos[1] + 1] == False and alphaVisited[mapArr[pos[0]][pos[1] + 1]] == False:
        dfs(mapArr, R, C, (pos[0], pos[1] + 1), N + 1, tempVisited, tempAlphaVisited)
    
    checkMaxValue(N)
    

R, C = map(int, input().split())
mapArr = []
for i in range(R):
    mapArr.append(list(input()))
    
alphaToInt = {} # alphaToInt['A']는 0, alphaToInt['B']는 1 과 같은 식으로 변환된다.
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    alphaToInt[alpha[i]] = i
    
# 알파벳으로 적힌 것을 숫자로 전부다 변환해 주고 탐색을 돌린다.    
for i in range(R):
    for j in range(C):
        mapArr[i][j] = alphaToInt[mapArr[i][j]]
       
visited = [[False for _ in range(C)] for _ in range(R)]
alphaVisited = [False] * 26

dfs(mapArr, R, C, (0, 0), 1, deepcopy(visited), deepcopy(alphaVisited))
        
print(maxValue)
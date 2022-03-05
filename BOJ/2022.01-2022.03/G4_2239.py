'''
스도쿠

입력
9개의 줄에 9개의 숫자로 보드가 입력된다.
아직 숫자가 채워지지 않은 칸에는 0이 주어진다.

출력
9개의 줄에 9개의 숫자로 답을 출력한다.
답이 여러 개 있다면 그 중 사전식으로 앞서는 것을 출력한다.
즉, 81자리의 수가 제일 작은 경우를 출력한다.
'''

'''
- 첫번째 줄 첫번째 열부터 DFS로 탐색해봐서 가능한 경우를 찾을 때까지 탐색해보자.
* Fail/1st/00:18:38/TimeOver
'''
from copy import deepcopy

def checkValid(arr, i, j, num): # i행 j열에 num숫자가 들어갈 수 있는지 넣기 전에 체크하는 함수
    if num in arr[i]:
        return False
    
    for k in range(9):
        if arr[k][j] == num:
            return False
        
    # i행 j열이 속한 3*3 블록에서 첫번째 칸의 인덱스
    a = i - (i % 3)
    b = j - (j % 3)
    
    for k1 in range(3):
        for k2 in range(3):
            if arr[a+k1][b+k2] == num:
                return False
            
    return True # 3가지 조건 모두 위배되지 않는 경우

def dfs(arr):
    tempArr = deepcopy(arr)
    
    # arr 중에 빈 칸(0)이 있는지 탐색
    for i in range(9):
        for j in range(9):
            if tempArr[i][j] == 0:
                # 빈 칸에 대해 1~9까지 수를 하나씩 시도
                for k in range(1, 10):
                    # 넣어도 규칙에 위배되지 않는다면 넣고 dfs 호출
                    if checkValid(tempArr, i, j, k):
                        tempArr[i][j] = k
                        result = dfs(tempArr)
                        if result != None:
                            return result
                    
                return None # 1~9까지 어느 수를 넣어도 답이 없는 경우 None 리턴
                    
    return tempArr

arr = []
for i in range(9):
    arr.append(list(map(int, list(input()))))

result = dfs(arr)

for i in range(9):
    for j in range(9):
        print(result[i][j], end="")
    if i != 9:
        print()
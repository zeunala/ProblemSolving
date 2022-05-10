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
- 시간을 좀 더 줄이기 위해 미리 각 행/열/정사각형 구간에 대해 숫자 존재 여부를 저장해서,
checkValid() 함수의 속도를 높여보자.
* Fail/2nd/00:49:15/TimeOver
- dfs함수를 좀 더 빠르게 하도록 수정하였다.
* Fail/3rd/00:58:46/TimeOver
- 자주 발생하는 연산을 좀 더 빠르게 수정하였다.
* Pass/4th/01:06:40(use PyPy3)
- 느린 deepcopy 연산 대신 재귀호출 후 원래 값으로 복구하는 방식이 시간을 단축시키는 것으로 보인다.
'''
from copy import deepcopy

def squareIdx(i, j): # i행 j열이 0~8번째 정사각형 중 몇 번째에 속하는지 리턴
    return (i // 3) * 3 + (j // 3)


def checkValid(rowNum, colNum, squNum, i, j, num): # i행 j열에 num숫자가 들어갈 수 있는지 넣기 전에 체크하는 함수
    if rowNum[i][num] or colNum[j][num] or squNum[squareIdx(i, j)][num]:
        return False
    else:
        return True

def dfs(arr, rowNum, colNum, squNum, i, j):
    if j >= 9:
        i += 1
        j = 0
    if i >= 9:
        return arr
    
    if arr[i][j] == 0:
        # 빈 칸에 대해 1~9까지 수를 하나씩 시도
        for k in range(1, 10):
            # 넣어도 규칙에 위배되지 않는다면 넣고 dfs 호출
            if checkValid(rowNum, colNum, squNum, i, j, k):
                arr[i][j] = k
                rowNum[i][k] = True
                colNum[j][k] = True
                squNum[squareIdx(i, j)][k] = True
                
                result = dfs(arr, rowNum, colNum, squNum, i, j + 1)
                if result != None:
                    return result
                else: # 만약 None이라면 이 k가 아니라는 것이므로 다시 복구
                    arr[i][j] = 0
                    rowNum[i][k] = False
                    colNum[j][k] = False
                    squNum[squareIdx(i, j)][k] = False
            
        return None # 1~9까지 어느 수를 넣어도 답이 없는 경우 None 리턴
    else:
        return dfs(arr, rowNum, colNum, squNum, i, j + 1)

arr = []
for i in range(9):
    arr.append(list(map(int, list(input()))))

rowNum = [[False for _ in range(10)] for _ in range(9)] # rowNum[a][b]는 a행(0~8)에 숫자 b(1~9)가 존재하는지 여부를 가리킨다.
colNum = [[False for _ in range(10)] for _ in range(9)] # 마찬가지로 각 열에 대해 저장
squNum = [[False for _ in range(10)] for _ in range(9)] # 마찬가지로 각 정사각형 구간에 대해 저장

for i in range(9):
    for j in range(9):
        rowNum[i][arr[i][j]] = True
        colNum[j][arr[i][j]] = True
        squNum[squareIdx(i,j)][arr[i][j]] = True

result = dfs(arr, rowNum, colNum, squNum, 0, 0)

for i in range(9):
    for j in range(9):
        print(result[i][j], end="")
    if i != 9:
        print()
'''
색종이 붙이기

입력
총 10개의 줄에 종이의 각 칸에 적힌 수가 주어진다.

출력
모든 1을 덮는데 필요한 색종이의 최소 개수를 출력한다. 1을 모두 덮는 것이 불가능한 경우에는 -1을 출력한다.
'''

'''
- 크기가 10*10 밖에 안되므로 모든 경우의 수를 다 탐색해볼 수 있다.
우선 0행부터 차례로 스캔하며 1을 만날 경우 5*5->4*4->...->1*1 순으로 색종이를 덮을 수 있는지 DFS로 모두 탐색해보자.
만약 큰 색종이로 덮을 수 있다고 해도 더 작은 걸로 덮었을 때 결국 총 색종이 수가 줄어들 수도 있으므로 주의해야 한다.
* Fail/1st/00:37:39/TimeOver
'''
from copy import deepcopy

def canUse(arr, N, a, b): # arr[a][b]부터 N*N 종이 자리가 있는지 체크해서 쓸 수 있다면 그 자리를 0으로 바꾼 배열 리턴. 자리가 없다면 None 리턴
    resultArr = deepcopy(arr)
    if a+(N-1) >= 10 or b+(N-1) >= 10: # 범위 넘길 수 없음
        return None

    for i in range(N):
        for j in range(N):
            if resultArr[a+i][b+j] == 1:
                resultArr[a+i][b+j] = 0
            else:
                return None
    
    return resultArr

def checkArea(arr, one, two, three, four, five): # arr과 현재까지 쓴 색종이 수들을 입력, 색종이 사용 개수 혹은 불가능시 -1 리턴
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1: # 종이로 덮어야 하는 부분 발견
                minPaper = 999
                if five < 5:
                    newArr = canUse(arr, 5, i, j)
                    if newArr != None:
                        newResult = checkArea(newArr, one, two, three, four, five + 1)
                        if newResult != -1 and minPaper > newResult:
                            minPaper = newResult
                if four < 5:
                    newArr = canUse(arr, 4, i, j)
                    if newArr != None:
                        newResult = checkArea(newArr, one, two, three, four + 1, five)
                        if newResult != -1 and minPaper > newResult:
                            minPaper = newResult
                if three < 5:
                    newArr = canUse(arr, 3, i, j)
                    if newArr != None:
                        newResult = checkArea(newArr, one, two, three + 1, four, five)
                        if newResult != -1 and minPaper > newResult:
                            minPaper = newResult
                if two < 5:
                    newArr = canUse(arr, 2, i, j)
                    if newArr != None:
                        newResult = checkArea(newArr, one, two + 1, three, four, five)
                        if newResult != -1 and minPaper > newResult:
                            minPaper = newResult
                if one < 5:
                    newArr = canUse(arr, 1, i, j)
                    if newArr != None:
                        newResult = checkArea(newArr, one + 1, two, three, four, five)
                        if newResult != -1 and minPaper > newResult:
                            minPaper = newResult
                
                if minPaper == 999: # 한번도 갱신 안됨 - 즉 색종이를 덮을 수 없음
                    return -1
                else:
                    return minPaper

    return one + two + three + four + five

arr = []
for i in range(10):
    arr.append(list(map(int, input().split())))

print(checkArea(arr, 0, 0, 0, 0, 0))
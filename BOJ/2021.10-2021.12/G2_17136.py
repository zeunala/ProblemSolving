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
- 모두 1이 되는 경우 등에서 5*5~1*1을 모두 다 탐색하려고 하니 시간이 너무 오래 걸린다.
큰 색종이를 먼저 쓰되 5*5를 전체 필드에서 덮고 -> 남은 필드에서 4*4를 전체 찾는 식으로 진행해보자.
* Fail/2nd/00:43:48/TimeOver
- 1이 많을 때 여전히 시간이 많이 걸리는 것으로 보아 가지를 좀 쳐내야 할 듯 하다.
중간에 1이 너무 많이 남았으면 None을 리턴하는 등의 처리를 추가하였다.
* Fail/3rd/01:15:03
- j값의 범위를 잘못 지정하는 실수를 발견하고 수정하였다.
* Fail/4th/01:29:13/TimeOver
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

def findOneNum(arr): # 1이 몇 개 있는지 리턴
    result = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                result += 1

    return result

def checkArea(arr, one, two, three, four, five, alreadyCheck, alreadyI, alreadyJ): # arr과 현재까지 쓴 색종이 수들을 입력, 색종이 사용 개수 혹은 불가능시 -1 리턴.
    if alreadyCheck >= 6: # 이미 5*5가능성을 다 확인했던 상태라면 패스
        if alreadyCheck == 6: # 기존 하던걸 이어서 체크한다.
            
            for i in range(alreadyI, 10):
                for j in range(10):
                    if arr[i][j] == 1: # 종이로 덮어야 하는 부분 발견
                        if five < 5:
                            newArr = canUse(arr, 5, i, j)
                            if newArr != None:
                                newResult = checkArea(newArr, one, two, three, four, five + 1, 6, i, j)
                                if newResult != -1:
                                    return newResult

    if alreadyCheck >= 5:
        if alreadyCheck == 5:
            for i in range(alreadyI, 10):
                for j in range(0, 10):
                    if arr[i][j] == 1:
                        if four < 5:
                            newArr = canUse(arr, 4, i, j)
                            if newArr != None:
                                newResult = checkArea(newArr, one, two, three, four + 1, five, 5, i, j)
                                if newResult != -1:
                                    return newResult
        else:
            for i in range(10):
                for j in range(10):
                    if arr[i][j] == 1:
                        if four < 5:
                            newArr = canUse(arr, 4, i, j)
                            if newArr != None:
                                newResult = checkArea(newArr, one, two, three, four + 1, five, 5, i, j)
                                if newResult != -1:
                                    return newResult

    if findOneNum(arr) > (3*3*(5-three) + 2*2*(5-two) + (5-one)): # 남은 색종이로 1을 절대로 덮을 수 없는 경우 굳이 더 안 찾고 -1 리턴
        return -1

    if alreadyCheck >= 4:
        if alreadyCheck == 4:
            for i in range(alreadyI, 10):
                for j in range(0, 10):
                    if arr[i][j] == 1:
                        if three < 5:
                            newArr = canUse(arr, 3, i, j)
                            if newArr != None:
                                newResult = checkArea(newArr, one, two, three + 1, four, five, 4, i, j)
                                if newResult != -1:
                                    return newResult
        else:
            for i in range(10):
                for j in range(10):
                    if arr[i][j] == 1:
                        if three < 5:
                            newArr = canUse(arr, 3, i, j)
                            if newArr != None:
                                newResult = checkArea(newArr, one, two, three + 1, four, five, 4, i, j)
                                if newResult != -1:
                                    return newResult

    if findOneNum(arr) > (2*2*(5-two) + (5-one)): # 남은 색종이로 1을 절대로 덮을 수 없는 경우 굳이 더 안 찾고 -1 리턴
        return -1

    if alreadyCheck >= 3:
        if alreadyCheck == 3:
            for i in range(alreadyI, 10):
                for j in range(0, 10):
                    if arr[i][j] == 1:
                        if two < 5:
                            newArr = canUse(arr, 2, i, j)
                            if newArr != None:
                                newResult = checkArea(newArr, one, two + 1, three, four, five, 3, i, j)
                                if newResult != -1:
                                    return newResult
        else:
            for i in range(10):
                for j in range(10):
                    if arr[i][j] == 1:
                        if two < 5:
                            newArr = canUse(arr, 2, i, j)
                            if newArr != None:
                                newResult = checkArea(newArr, one, two + 1, three, four, five, 3, i, j)
                                if newResult != -1:
                                    return newResult

    if findOneNum(arr) > (5-one): # 남은 색종이로 1을 절대로 덮을 수 없는 경우 굳이 더 안 찾고 -1 리턴
        return -1

    if alreadyCheck >= 2:
        if alreadyCheck == 2:
            for i in range(alreadyI, 10):
                for j in range(0, 10):
                    if arr[i][j] == 1:
                        if one < 5:
                            newArr = canUse(arr, 1, i, j)
                            if newArr != None:
                                newResult = checkArea(newArr, one + 1, two, three, four, five, 2, i, j)
                                if newResult != -1:
                                    return newResult
                        return -1 # 색종이로 덮을 수 없는 경우 여기 도달한다.
        else:
            for i in range(10):
                for j in range(10):
                    if arr[i][j] == 1:
                        if one < 5:
                            newArr = canUse(arr, 1, i, j)
                            if newArr != None:
                                newResult = checkArea(newArr, one + 1, two, three, four, five, 2, i, j)
                                if newResult != -1:
                                    return newResult
                        return -1 # 색종이로 덮을 수 없는 경우 여기 도달한다.
                
    return one + two + three + four + five

arr = []
for i in range(10):
    arr.append(list(map(int, input().split())))

print(checkArea(arr, 0, 0, 0, 0, 0, 6, 0, 0))
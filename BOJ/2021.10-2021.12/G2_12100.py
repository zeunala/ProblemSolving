'''
2048 (Easy)

입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다.
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다.
블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
'''

'''
- 우선 이동시켰을 때 결과 보드를 반환하는 함수를 만들고 상하좌우 총 4^5 개의 경우의 수를 모두 체크하여 그 중 가장 큰 블록을 출력해보자.
* Pass/1st/00:34:15
'''
from copy import deepcopy
from itertools import product

def findMaxValue(arr, N):
    maxValue = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > maxValue:
                maxValue = arr[i][j]
                
    return maxValue

def moveBoard(arr, N, direction): # direction 1,2,3,4는 각각 상,하,좌,우에 대응된다.
    tempArr = deepcopy(arr)
    resultArr = [[0 for _ in range(N)] for _ in range(N)]
    
    if direction == 1:
        for i in range(N):
            arrExceptZero = []
            tempLine = []
            
            for j in range(N):
                if tempArr[j][i] != 0:
                    arrExceptZero.append(tempArr[j][i])
            
            j = 0
            while j < len(arrExceptZero) - 1:
                if arrExceptZero[j] == arrExceptZero[j + 1]:
                    tempLine.append(arrExceptZero[j] * 2)
                    j += 1
                else:
                    tempLine.append(arrExceptZero[j])
                j += 1
            if j == len(arrExceptZero) - 1:
                tempLine.append(arrExceptZero[-1]) # 마지막 원소도 넣음
            
            for j in range(len(tempLine)):
                resultArr[j][i] = tempLine[j]
                
    elif direction == 2:
        for i in range(N):
            arrExceptZero = []
            tempLine = []
            
            for j in range(N-1, -1, -1):
                if tempArr[j][i] != 0:
                    arrExceptZero.append(tempArr[j][i])
            
            j = 0
            while j < len(arrExceptZero) - 1:
                if arrExceptZero[j] == arrExceptZero[j + 1]:
                    tempLine.append(arrExceptZero[j] * 2)
                    j += 1
                else:
                    tempLine.append(arrExceptZero[j])
                j += 1
            if j == len(arrExceptZero) - 1:
                tempLine.append(arrExceptZero[-1]) # 마지막 원소도 넣음
            
            for j in range(len(tempLine)):
                resultArr[(N-1)-j][i] = tempLine[j]
                
    elif direction == 3: # 우선 가장 직관적인 왼쪽 방향부터 구현하고 나머지는 인덱스값만 적당히 바꿔주면 된다.
        for i in range(N):
            arrExceptZero = []
            tempLine = []
            
            for j in range(N):
                if tempArr[i][j] != 0:
                    arrExceptZero.append(tempArr[i][j])
            
            j = 0
            while j < len(arrExceptZero) - 1:
                if arrExceptZero[j] == arrExceptZero[j + 1]:
                    tempLine.append(arrExceptZero[j] * 2)
                    j += 1
                else:
                    tempLine.append(arrExceptZero[j])
                j += 1
            if j == len(arrExceptZero) - 1:
                tempLine.append(arrExceptZero[-1]) # 마지막 원소도 넣음
            
            for j in range(len(tempLine)):
                resultArr[i][j] = tempLine[j]
            
    elif direction == 4:
        for i in range(N):
            arrExceptZero = []
            tempLine = []
            
            for j in range(N-1, -1, -1):
                if tempArr[i][j] != 0:
                    arrExceptZero.append(tempArr[i][j])
            
            j = 0
            while j < len(arrExceptZero) - 1:
                if arrExceptZero[j] == arrExceptZero[j + 1]:
                    tempLine.append(arrExceptZero[j] * 2)
                    j += 1
                else:
                    tempLine.append(arrExceptZero[j])
                j += 1
            if j == len(arrExceptZero) - 1:
                tempLine.append(arrExceptZero[-1]) # 마지막 원소도 넣음
            
            for j in range(len(tempLine)):
                resultArr[i][(N-1)-j] = tempLine[j]
    
    return resultArr
    
N = int(input())
field = []
answer = 0
for i in range(N):
    field.append(list(map(int, input().split())))
    
for e in list(product(range(1,5), range(1,5), range(1,5), range(1,5), range(1,5))):
    (a1, a2, a3, a4, a5) = e
    after1 = moveBoard(field, N, a1)
    after2 = moveBoard(after1, N, a2)
    after3 = moveBoard(after2, N, a3)
    after4 = moveBoard(after3, N, a4)
    after5 = moveBoard(after4, N, a5)
    
    result = findMaxValue(after5, N)
    if answer < result:
        answer = result
        
print(answer)
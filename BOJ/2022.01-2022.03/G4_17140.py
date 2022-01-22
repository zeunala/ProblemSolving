'''
이차원 배열과 연산

입력
첫째 줄에 r, c, k가 주어진다. (1 ≤ r, c, k ≤ 100)
둘째 줄부터 3개의 줄에 배열 A에 들어있는 수가 주어진다. 배열 A에 들어있는 수는 100보다 작거나 같은 자연수이다.

출력
A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간을 출력한다. 100초가 지나도 A[r][c] = k가 되지 않으면 -1을 출력한다
'''

'''
- 문제의 요구사항 그대로 구현을 해보자.
모든 열에 대해 정렬하는 경우 T연산을 만들어 행과 열을 바꾼 후 정렬하고 이후 다시 원래상태로 돌려놓자.
* Pass/1st/00:35:32
'''
from collections import Counter

def makeArrT(arr):
    columnNum = len(arr[0])
    rowNum = len(arr)
    resultArr = []
    for i in range(columnNum):
        tempArr = []
        for j in range(rowNum):
            tempArr.append(arr[j][i])
        resultArr.append(tempArr)
        
    return resultArr

def makeArrR(arr): # 배열에 대해 R연산을 수행한다.
    resultArr = []
    maxColumnNum = 0
    for i in range(len(arr)):
        tempDict = dict(Counter(arr[i])) # 각 행에 대해 수가 몇 번 나왔는지 확인
        tempArr = [(e, tempDict[e]) for e in tempDict.keys() if e != 0]
        tempArr.sort(key = lambda x : (x[1], x[0])) # 나오는 횟수가 적은게 우선, 횟수가 같으면 수가 작은게 우선
        
        tempArr2 = [] # tempArr의 튜플을 원소단위로 쪼갬
        for (a, b) in tempArr:
            tempArr2.append(a)
            tempArr2.append(b)
        resultArr.append(tempArr2)
        
        if maxColumnNum < len(tempArr2):
            maxColumnNum = len(tempArr2)
        
    if maxColumnNum > 100: # 최대 100줄
        maxColumnNum = 100
    
    # 가장 행이 긴걸 기준으로 자름
    for i in range(len(resultArr)):
        if len(resultArr[i]) > maxColumnNum:
            resultArr[i] = resultArr[i][:maxColumnNum]
        elif len(resultArr[i]) < maxColumnNum:
            need = maxColumnNum - len(resultArr[i]) # 그만큼 뒤에 0을 더 붙여주어야 한다.
            for j in range(need):
                resultArr[i].append(0)
                
    return resultArr


def sortArr(arr): # 배열에 대해 정렬을 수행한다.
    columnNum = len(arr[0])
    rowNum = len(arr)
    
    if rowNum >= columnNum: # R연산
        return makeArrR(arr)
    else: # C연산
        arrT = makeArrT(arr) # 행과 열을 바꾸고
        arrT = makeArrR(arrT) # 행에 대해 정렬 수행
        return makeArrT(arrT) # 다시 행과 열을 바꿔서 리턴
    
r, c, k = map(int, input().split())
A = []
for i in range(3):
    A.append(list(map(int, input().split())))

answer = -1
for i in range(101):
    if r-1 < len(A) and c-1 < len(A[0]) and A[r-1][c-1] == k:
        answer = i
        break
    else:
        A = sortArr(A)

print(answer)
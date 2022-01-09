'''
후보키

- 입력 범위가 작으므로 모든 경우의 수 하나하나 체크해보자.
각 속성들에 대한 경우의 수에 대하여 중복되는게 없으면 후보로 오르고,
이들중 최소성을 만족하면서 후보 키의 최대 개수인 것을 선택한다.
* Fail/1st/00:28:20
'''

from itertools import product

def checkDuplicate(relation, column):
    arr = []
    for e in relation:
        temp = []
        for e2 in column:
            temp.append(e[e2])
        arr.append(tuple(temp))
    
    # 결국 arr에는 기존 relation배열에서 column들에 해당하는 것만 취한 것이 된다.
    # 이 때 relation과는 달리 각 원소는 튜플이다.
    
    if len(arr) == len(set(arr)): # 중복되는 원소 있는지 체크
        return True
    else:
        return False
  
columnArr = [] # 유일성을 만족하는 column쌍들의 집합

def dfs(relation, arr, start, end): # 만약 열이 5개 있다면 start = 0, end = 4에서 시작
    if start == end:
        if checkDuplicate(relation, arr):
            global columnArr
            columnArr.append(arr)
    else:
        dfs(relation, arr, start + 1, end)
        dfs(relation, arr + [start], start + 1, end)


def solution(relation):
    answer = 0
    
    column = len(relation[0])
    row = len(relation)
    
    dfs(relation, [], 0, column - 1)
    
    # 유일성 만족하는 쌍들 중 길이가 큰 것부터 체크
    columnArr.sort(key = lambda x : len(x), reverse = True)
    
    for e in columnArr:
        isMinimal = True # 최소성 만족 여부
        for i in range(len(e)):
            # 하나 뺐는데 columnArr에 존재시 최소성 위배
            if (e[:i] + e[i+1:]) in columnArr:
                isMinimal = False
        if isMinimal:
            return len(e)
    
    return 0
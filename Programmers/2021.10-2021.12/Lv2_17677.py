'''
뉴스 클러스터링

- 다중집합을 사용하기 위해 딕셔너리를 이용한다.
* Pass/1st/00:17:29
'''
def isAlpha(str):
    if str[0].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and str[1].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    else:
        return False

def solution(str1, str2):
    arr1 = {}
    arr2 = {}
    intersectArr = {}
    unionArr = {}
    
    # 유효한 문자열을 각각 arr1, arr2에 넣는다.
    for i in range(len(str1) - 1):
        temp = str1[i:i+2].upper()
        if isAlpha(temp):
            if temp in arr1:
                arr1[temp] += 1
            else:
                arr1[temp] = 1
    
    for i in range(len(str2) - 1):
        temp = str2[i:i+2].upper()
        if isAlpha(temp):
            if temp in arr2:
                arr2[temp] += 1
            else:
                arr2[temp] = 1
                
    # arr1, arr2 원소에 대해서 interSectArr, unionArr에 원소를 넣는다.
    for e in list(arr1.keys()):
        if e in arr2:
            intersectArr[e] = min(arr1[e], arr2[e]) # 작은 값을 넣음
            unionArr[e] = max(arr1[e], arr2[e]) # 큰 값을 넣음
        else:
            unionArr[e] = arr1[e]
    
    for e in list(arr2.keys()):
        if e not in arr1: # arr1에 없는 것들만 합집합에 넣어주면 된다.
            unionArr[e] = arr2[e]
    
    if unionArr == {}:
        unionSum = 0
    else:
        unionSum = sum(list(unionArr.values()))
    
    if intersectArr == {}:
        intersectSum = 0
    else:
        intersectSum = sum(list(intersectArr.values()))
    
    if unionSum == 0:
        return 65536
    else:
        return intersectSum * 65536 // unionSum
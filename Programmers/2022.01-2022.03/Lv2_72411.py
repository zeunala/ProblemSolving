'''
메뉴 리뉴얼

- combinations를 이용해 각 조합을 가져와 가장 많은 것을 선택한다.
* Fail/1st/00:20:24/TimeOver
- orders배열에 대해 전처리를 해서 좀 더 빠르도록 변경하였다.
* Fail/2nd/00:34:37/TimeOver
- 시간을 줄이도록 가지치기를 추가하였다.
* Fail/3rd/00:54:15/TimeOver
- 집합연산을 이용하여 좀 더 빠르게 하도록 수정하였다.
* Fail/4th/01:02:43/TimeOver
'''

from itertools import combinations

def solution(orders, course):
    answer = []
    allAlphabets = [] # orders에 들어있는 모든 알파벳들
    
    for e in orders:
        for e2 in e:
            if e2 not in allAlphabets:
                allAlphabets.append(e2)
    allAlphabets.sort()
    
    ordersCompiled = [set([]) for _ in range(len(orders))]
    for i in range(len(orders)):
        for e in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if e in orders[i]:
                ordersCompiled[i].add(e)

    for x in range(2, 11):
        allAlphaCombinationTemp = list(combinations(allAlphabets, x))
        allAlphaCombination = []
        for t in allAlphaCombinationTemp:
            temp = ""
            for t2 in t:
                temp += t2
            allAlphaCombination.append(temp)
        
        tempDict = {} # 각 조합들이 몇 번 나오는지
        for e in allAlphaCombination:
            tempDict[e] = 0
        
        maxCount = 0
        for e in allAlphaCombination:
            for f in range(len(ordersCompiled)):
                isInCombination = True # 각 조합들이 orders의 각 항목에 있는지 여부
                if len(e) >= 2 and e[:-1] not in ordersCompiled[f]: # 가지치기 추가
                    continue
                for e2 in e:
                    if e2 not in ordersCompiled[f]:
                        isInCombination = False
                        break
                if isInCombination:
                    tempDict[e] += 1
                    ordersCompiled[f].add(e) # 가지치기 위해 가능한 조합 추가
                    if maxCount < tempDict[e]:
                        maxCount = tempDict[e]
        
        if maxCount > 1 and x in course:
            for e in allAlphaCombination:
                if tempDict[e] == maxCount:
                    answer.append(e)
    
    answer.sort()
    return answer
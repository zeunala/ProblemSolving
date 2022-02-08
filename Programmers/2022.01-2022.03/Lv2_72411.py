'''
메뉴 리뉴얼

- combinations를 이용해 각 조합을 가져와 가장 많은 것을 선택한다.
* Fail/1st/00:20:24/TimeOver
- orders배열에 대해 전처리를 해서 좀 더 빠르도록 변경하였다.
* Fail/2nd/00:34:37/TimeOver
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
    
    ordersCompiled = [{} for _ in range(len(orders))]
    for i in range(len(orders)):
        for e in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if e in orders[i]:
                ordersCompiled[i][e] = True
            else:
                ordersCompiled[i][e] = False
    
    for e in course:
        allAlphaCombinationTemp = list(combinations(allAlphabets, e))
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
            for f in ordersCompiled:
                isInCombination = True # 각 조합들이 orders의 각 항목에 있는지 여부
                for e2 in e:
                    if not f[e2]:
                        isInCombination = False
                        break
                if isInCombination:
                    tempDict[e] += 1
                    if maxCount < tempDict[e]:
                        maxCount = tempDict[e]
        
        for e in allAlphaCombination:
            if tempDict[e] == maxCount and maxCount > 1:
                answer.append(e)
        
    answer.sort()
    return answer
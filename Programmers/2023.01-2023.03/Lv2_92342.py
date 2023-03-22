'''
양궁대회

- n이 최대 10뿐이므로 모든 경우의 수를 체크하도록 한다.
* Pass/1st/00:27:26
'''
from itertools import combinations_with_replacement

def calcScore(enemyInfo, playerInfo): # 화살개수가 주어질 때 라이언-어피치 득점차를 리턴
    enemyScore = 0
    playerScore = 0
    
    for i in range(10, 0, -1): # 10점부터 1점까지 계산
        if enemyInfo[10 - i] == 0 and playerInfo[10 - i] == 0:
            continue
        
        if enemyInfo[10 - i] >= playerInfo[10 - i]:
            enemyScore += i
        else:
            playerScore += i
    
    return playerScore - enemyScore

def caseToInfo(case): # ex. (0, 1, 1, 9) -> [0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1]
    result = [0] * 11
    for e in case:
        result[10 - e] += 1
        
    return result

def solution(n, info):
    maxScore = 0
    answer = [-1]
    
    # 가장 낮은 점수를 더 많이 맞힌 경우부터 탐색하게 된다.
    for case in list(combinations_with_replacement(range(11), r = n)):
        playerInfo = caseToInfo(case)
        
        currentScore = calcScore(info, playerInfo)
        if maxScore < currentScore:
            maxScore = currentScore
            answer = playerInfo
        
    return answer
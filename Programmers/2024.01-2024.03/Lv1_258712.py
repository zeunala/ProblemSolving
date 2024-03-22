'''
가장 많이 받은 선물

- 각 사람 별로 선물 지수와 친구들마다 받은 선물의 수를 기록하고,
모든 두 사람의 짝에 대해 선물을 주고 받는걸 확인하면 된다.
* Pass/1st/00:14:21
'''
from collections import defaultdict
from itertools import combinations

def solution(friends, gifts):
    friendArr = dict() # 각 사람별 받은 친구들마다의 선물 수
    friendCount = defaultdict(int) # 각 사람마다의 선물 지수
    friendNextCount = dict() # 각 사람마다 다음 달에 받을 개수
    
    for name in friends:
        friendArr[name] = defaultdict(int)
        friendNextCount[name] = 0
    
    for giftLine in gifts:
        a, b = giftLine.split() # a가 준 사람, b가 받은 사람
        friendArr[b][a] += 1
        friendCount[a] += 1
        friendCount[b] -= 1
        
    for (a, b) in list(combinations(friends, 2)):
        if friendArr[a][b] > friendArr[b][a]: # a가 받은게 더 많음
            friendNextCount[b] += 1
        elif friendArr[b][a] > friendArr[a][b]:
            friendNextCount[a] += 1
        elif friendCount[a] > friendCount[b]:
            friendNextCount[a] += 1
        elif friendCount[b] > friendCount[a]:
            friendNextCount[b] += 1
        
    return max(friendNextCount.values())
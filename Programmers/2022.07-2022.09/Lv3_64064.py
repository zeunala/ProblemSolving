'''
불량 사용자

- 배열의 크기가 적으므로 순열을 이용해서 모든 경우의 수를 체크한다.
* Pass/1st/00:14:52
'''

from itertools import permutations

def checkId(user_id, banned_id): # ex. "frodo"와 "fr*d*"와 매칭되는지 여부를 체크
    result = True
    
    if len(user_id) != len(banned_id):
        return False
    
    for i in range(len(user_id)):
        if user_id[i] == banned_id[i] or banned_id[i] == "*":
            continue
        else:
            result = False
            break
            
    return result
        
    
def solution(user_id, banned_id):
    answer = set()
    
    # user_id에서 banned_id개수만큼 뽑아서 모든 경우의 수에 대해 직접 대조해본다.
    for e in list(permutations(range(len(user_id)), len(banned_id))):
        valid = True
        
        # ex. e가 (3, 4)일 경우, user_id[3], user_id[4]가 banned_id 첫, 두번재에 매칭되는지 확인한다는 것을 의미한다.
        for i in range(len(e)):
            if checkId(user_id[e[i]], banned_id[i]):
                continue
            else:
                valid = False
                break
                
        # 예를 들어 (1,0,2)와 (2,0,1)은 동일한 경우이므로 집합으로 걸러냄
        if valid:
            answer.add(tuple(sorted(list(e))))
        
    return len(answer)
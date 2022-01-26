'''
자물쇠와 열쇠

- M, N 범위가 작으므로 모든 경우의 수를 모두 계산해보자.
이 때 key를 90도, 180도, 270도 돌리는 경우도 생각해야 한다.
* Pass/1st/00:19:21
'''
from copy import deepcopy

def checkLockCorrect(lock): # lock의 모든 수가 1인지 여부를 리턴
    for e in lock:
        for e2 in e:
            if e2 != 1:
                return False
    return True

def checkKeyLock(key, lock): # key가 lock에 맞을 수 있는지 리턴. 이 때 돌리는 경우는 생각X
    for moveX in range(-len(lock) + 1, len(lock)): # key를 x만큼 움직인다.
        for moveY in range(-len(lock) + 1, len(lock)): # key를 y만큼 움직인다.
            copyLock = deepcopy(lock) # key와 lock을 더한 배열
            for i in range(len(key)):
                for j in range(len(key)):
                    if i + moveY >= 0 and i + moveY < len(copyLock) and j + moveX >= 0 and j + moveX < len(copyLock):
                        copyLock[i + moveY][j + moveX] += key[i][j]
            
            if checkLockCorrect(copyLock):
                return True
    
    return False
                    
def rollKey(key): # key를 시계방향으로 한 번 돌린 배열을 리턴한다.
    result = deepcopy(key)
    
    for i in range(len(key)):
        for j in range(len(key)):
            result[j][len(key) - 1 - i] = key[i][j]
            
    return result
    
def solution(key, lock):
    # 각각 key를 0~3번 돌린 배열
    key0 = key
    key1 = rollKey(key0)
    key2 = rollKey(key1)
    key3 = rollKey(key2)
    
    if checkKeyLock(key0, lock) or checkKeyLock(key1, lock) or checkKeyLock(key2, lock) or checkKeyLock(key3, lock):
        return True
    else:
        return False
    
    return answer
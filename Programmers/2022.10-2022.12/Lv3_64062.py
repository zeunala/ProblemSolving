'''
징검다리 건너기

- 건널 수 있는 사람의 수가 최대 k명이라면 k명까지는 OK이고 k+1명부터 건널 수 없으므로,
파라매트릭 서치를 이용하여 0~2억 범위를 좁혀나가도록 한다.
* Fail/1st/00:07:08
'''
def isSafe(stones, k): # k명이 건널 수 있는지 여부를 리턴
    for i in range(len(stones) - 2): # 3개 연속 k미만이면 k번째로는 건널 수 없다.
        if stones[i] < k and stones[i + 1] < k and stones[i + 2] < k:
            return False
    return True
    
    
def solution(stones, k):
    answer = 0
    minValue = 0
    maxValue = 200000000
    
    while minValue <= maxValue:
        midValue = (minValue + maxValue) // 2
        if isSafe(stones, midValue):
            if answer < midValue:
                answer = midValue
            minValue = midValue + 1
        else:
            maxValue = midValue - 1
    
    return answer
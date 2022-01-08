'''
실패율

- 주어진 문제 그대로 구현하면 될 것으로 보인다.
* Fail/1st/00:11:35
'''
def getSuccess(targetStage, stages): # targetStage를 클리어한 사람 수 리턴
    return len([stages[i] for i in range(len(stages)) if stages[i] > targetStage])

def getFail(targetStage, stages): # targetStage에 도전했지만 실패한 사람 수 리턴
    return len([stages[i] for i in range(len(stages)) if stages[i] == targetStage])


def solution(N, stages):
    answer = []
    arr = [] # (실패율, 스테이지번호)의 튜플이 오게 함. 이 때 실패율은 -로 넣어 sort시 내림차순이 되도록 한다.
    for i in range(1, N + 1):
        successNum = getSuccess(i, stages)
        failNum = getFail(i, stages)
        arr.append((-(failNum / (successNum + failNum)), i))
        
    arr.sort()
    
    for (a, b) in arr:
        answer.append(b)
    
    return answer
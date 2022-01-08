'''
실패율

- 주어진 문제 그대로 구현하면 될 것으로 보인다.
* Fail/1st/00:11:35
- 스테이지에 도전한 사람이 없을 경우 0으로 나누게 되어 오류가 발생한 것으로 보여 수정하였다.
* Fail/2nd/00:21:48/TimeOver
- 시간초과가 나지 않도록 한단계 더 최적화를 수행하였다.
* Pass/3rd/00:27:48
'''
def solution(N, stages):
    answer = []
    
    success = [0 for _ in range(N+2)] # success[i]는 i번째 stage를 성공한 사람 수
    fail = [0 for _ in range(N+2)] # fail[i]는 i번째 stage를 성공한 사람 수
    
    for e in stages:
        # stages의 원소가 e라는 것은 e-1번째 stage까지 성공하고 e번째 stage는 실패했다는 의미가 됨.
        # 편의상 마지막 N번째 stage까지 성공했을 경우 N+1번째 stage를 실패했다고 하자.
        success[e-1] += 1
        fail[e] += 1
    
    for i in range(N, 0, -1):
        # i번째 stage를 성공했다는 것은 i-1번째 stage도 성공했다는 것이므로 뒤에서부터 누적해서 더해준다.
        success[i] += success[i+1]
        
    
    arr = [] # (실패율, 스테이지번호)의 튜플이 오게 함. 이 때 실패율은 -로 넣어 sort시 내림차순이 되도록 한다.
    for i in range(1, N + 1):
        if success[i] + fail[i] == 0:
            arr.append((0, i))
        else:
            arr.append((-(fail[i] / (success[i] + fail[i])), i))
        
    arr.sort()
    
    for (a, b) in arr:
        answer.append(b)
    
    return answer
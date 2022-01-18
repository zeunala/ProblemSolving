'''
추석 트래픽

- 우선 시간/밀리초를 하나의 숫자가 되도록 바꾸고,
각 문자열에 대해서 이전과 겹치는 게 총 몇 개 있는지 체크하여, 초당 최대 처리량을 갱신한다.
* Fail/1st/00:30:59
- 다른 방식으로 풀어보자.
우선 시간/밀리초를 하나의 숫자가 되도록 바꾸고,
각 문자열에 대하여 시작시간/종료시간을 저장해둔다.
이후 그 시작시간, 종료시간들을 후보로 1초간 처리량을 계산한다.
* Pass/2nd/00:57:29
'''
def timeToNum(time): # time예시: "01:00:04.001"
    arr = time.split(":")
    hour = int(arr[0])
    minute = int(arr[1])
    second = int(arr[2][:-4])
    mSecond = int(arr[2][-3:])
    
    totalTime = 0
    totalTime += hour
    totalTime *= 60
    totalTime += minute
    totalTime *= 60
    totalTime += second
    totalTime *= 1000
    totalTime += mSecond
    
    return totalTime

def checkTime(target, base): # target의 시작시점~끝시점 안에 base~1초와 겹치는지
    (startTime, endTime) = target
    if endTime < base or startTime > base + 999:
        return False
    else:
        return True
    
def solution(lines):
    answer = 1
    arr = [] # 각 원소는 (시작시점, 끝시점)의 튜플이다.
    targetTime = [] # 최대 처리량을 계산할 시점
    for e in lines:
        e2 = e.split()
        startTime = timeToNum(e2[1]) - int(float(e2[2][:-1])*1000) + 1
        endTime = timeToNum(e2[1])
        arr.append((startTime, endTime))
        
        targetTime.append(startTime)
        targetTime.append(endTime)
    
    arr.sort()
    
    for e in targetTime:
        temp = 0
        for e2 in arr:
            if checkTime(e2, e):
                temp += 1
        if answer < temp:
            answer = temp

    return answer
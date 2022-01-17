'''
셔틀버스

- 우선 마지막 버스가 9시 + t * (n-1)분에 오므로 적어도 그 안에 와야 하며,
또한 마지막 버스를 타는 인원 중 선착순 m명에 들어야 무사히 탈 수 있다.
* Fail/1st/00:30:45
'''
def timeToNum(time): # 예를 들어 "08:45"는 8*60+45의 int 값을 리턴한다.
    a, b = map(int, time.split(":"))
    return a * 60 + b

def numToTime(num): # 예를 들어 150은 "02:30"의 string 값을 리턴한다.
    a = num // 60
    b = num % 60
    
    result = ""
    if a < 10:
        result += "0" + str(a)
    else:
        result += str(a)
    result += ":"
    
    if b < 10:
        result += "0" + str(b)
    else:
        result += str(b)
    
    return result

def solution(n, t, m, timetable):
    answer = 0
    
    numtable = [] # timetable을 숫자로 바꿔 정렬한 배열
    for e in timetable:
        numtable.append(timeToNum(e))
    numtable.sort(reverse = True) # pop 했을 때 먼저 온 사람부터 나가도록 함
    
    lastBusTime = timeToNum("09:00") + (n - 1) * t # 마지막으로 버스 오는 시간
    
    answer = lastBusTime # 마지막 버스 이전에는 와야 한다.

    for i in range(n - 1): # i번째 버스(마지막 버스를 제외하고 확인함)
        for j in range(m): # 각 버스는 버스 시간에 맞춘 사람을 m명까지 태운다.
            if numtable and numtable[-1] <= timeToNum("09:00") + (i - 1) * t:
                numtable.pop()
            else:
                break
    
    if len(numtable) < m: # 어떤 경우에도 내 앞에 m명 오는 경우
        pass
    else:
        if answer > numtable[-m] - 1:
            answer = numtable[-m] - 1 # m번째 사람보다는 1분 빨리 와야함
    
    return numToTime(answer)
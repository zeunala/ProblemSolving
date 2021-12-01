'''
추석 트래픽

- 우선 시간/밀리초를 하나의 숫자가 되도록 바꾸고,
각 문자열에 대해서 이전과 겹치는 게 총 몇 개 있는지 체크하여, 초당 최대 처리량을 갱신한다.
* Fail/1st/00:30:59
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
    

def solution(lines):
    answer = 1
    arr = []
    for e in lines:
        e2 = e.split()
        arr.append((timeToNum(e2[1]), int(float(e2[2][:-1])*1000)))
    
    for i in range(len(arr)):
        temp = 1
        for j in range(i-1, -1, -1):
            if arr[i][0] - arr[j][0] < arr[i][1] + 999:
                temp += 1
            else:
                break
        if answer < temp:
            answer = temp

    return answer
'''
다트 게임

- 문제 그대로 구현만 하면 된다. 문자열을 배열로 잘 옮기는 것에 신경쓰자.
* Pass/1st/00:17:18
'''

def solution(dartResult):
    answer = 0
    
    arr = [] # (점수, 영역, 옵션)의 튜플 존재
    i = 0
    while i < len(dartResult):
        score = int(dartResult[i])
        if dartResult[i + 1] == '0': # 10이 입력으로 들어간 경우 생각
            score = 10
            i += 1
        i += 1
        
        area = dartResult[i]
        i += 1
        
        if i >= len(dartResult): # 옵션 없이 문자열 끝 도달 상황의 경우
            arr.append((score, area, None))
            break
        
        if dartResult[i] != "*" and dartResult[i] != '#': # 옵션 없을 경우
            arr.append((score, area, None))
        else:
            arr.append((score, area, dartResult[i]))
            i += 1
        
    scoreArr = [arr[i][0] for i in range(len(arr))]
    print(scoreArr)
    
    for i in range(len(arr)):
        if arr[i][1] == "D":
            scoreArr[i] = scoreArr[i] ** 2
        elif arr[i][1] == "T":
            scoreArr[i] = scoreArr[i] ** 3
        
        if arr[i][2] == "*":
            scoreArr[i] *= 2
            if i > 0:
                scoreArr[i-1] *= 2
        elif arr[i][2] == "#":
            scoreArr[i] *= -1
        
    return sum(scoreArr)
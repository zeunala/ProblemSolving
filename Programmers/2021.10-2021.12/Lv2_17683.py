'''
방금그곡

- 주어진 조건에 따라 악보를 구하고 문자열 비교를 통해 조건에 일치하는 음악들을 찾는다.
이후 조건에 일치하는 음악들 중 우선순위가 가장 높은 걸 반환하면 된다.
이 때 C와 C#등을 구분하기 위해 기존 C를 C0으로 변환한다.
* Fail/1st/00:34:37
- 조건 일치 음악이 여러 개일 때 시간이 제일 긴 것을 반환해야 하는데 이 부분을 실수하여 수정하였다.
* Pass/2nd/00:36:02
'''
def getTime(start, end): # 음악 길이를 반환
    startHour, startMinute = map(int, start.split(":"))
    endHour, endMinute = map(int, end.split(":"))
    
    return (endHour * 60 + endMinute) - (startHour * 60 + startMinute)

def getMusic(defaultMusic, length): # 악보 문자열 반환
    idx = 0
    result = ""
    remainLength = length
    
    while remainLength > 0:
        current = defaultMusic[idx]
        
        if idx + 1 < len(defaultMusic) and defaultMusic[idx + 1] == "#":
            current += defaultMusic[idx + 1]
            idx += 2
        else:
            current += "0"
            idx += 1
            
        result += current
        remainLength -= 1
        
        if idx >= len(defaultMusic):
            idx = 0
            
    return result

def solution(m, musicinfos):
    correctMusic = [] # 조건에 일치하는 음악의 (재생시간, 입력순서, 음악제목)의 튜플이 담긴다.
    
    formattedM = ""
    
    i = 0
    while i < len(m):
        if i + 1 < len(m) and m[i + 1] == "#":
            formattedM += (m[i] + m[i + 1])
            i += 2
        else:
            formattedM += (m[i] + "0")
            i += 1
    
    
    for i in range(len(musicinfos)):
        start, end, name, defaultMusic = musicinfos[i].split(",")
        
        currentMusic = getMusic(defaultMusic, getTime(start, end))
        
        if formattedM in currentMusic:
            correctMusic.append((getTime(start, end), i, name))
        
    if correctMusic:
        correctMusic.sort()
        return correctMusic[0][2]
    else:
        return "(None)"
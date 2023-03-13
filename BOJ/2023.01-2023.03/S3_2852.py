'''
NBA 농구

입력
첫째 줄에 골이 들어간 횟수 N(1<=N<=100)이 주어진다.
둘째 줄부터 N개의 줄에 득점 정보가 주어진다.
득점 정보는 득점한 팀의 번호와 득점한 시간으로 이루어져 있다.
팀 번호는 1 또는 2이다. 득점한 시간은 MM:SS(분:초) 형식이며, 분과 초가 한자리 일 경우 첫째자리가 0이다.
분은 0보다 크거나 같고, 47보다 작거나 같으며, 초는 0보다 크거나 같고, 59보다 작거나 같다.
득점 시간이 겹치는 경우는 없다.

출력
첫째 줄에 1번 팀이 이기고 있던 시간, 둘째 줄에 2번 팀이 이기고 있던 시간을 출력한다. 시간은 입력과 같은 형식(MM:SS)으로 출력한다.
'''

'''
- 문제의 요구사항을 그대로 구현하면 되는 문제이다. 분+초를 초단위로 전부 바꿔서 구현하기 편하도록 한다.
* Pass/1st/00:17:12
'''
def timeToNum(timeStr): # "01:10"과 같은 시간 문자열을 초단위의 정수로 바꾼다. (ex. "00:00" -> 0, "10:00" -> 600)
    minute, second = map(int, timeStr.split(":"))
    return minute * 60 + second

def numToTime(num): # 반대로 초단위의 정수를 시간 문자열로 바꾼다.
    minute = str(num // 60)
    second = str(num % 60)
    if len(minute) == 1:
        minute = "0" + minute
    if len(second) == 1:
        second = "0" + second   
    return minute + ":" + second
    
N = int(input())
scoreDict = {} # 시간을 key값, 득점한 팀 번호를 value로 한다. (득점 시간이 겹치지 않는다 했으므로)

for i in range(N):
    teamNo, timeStr = input().split()
    scoreDict[timeToNum(timeStr)] = int(teamNo)

teamWinTime1 = 0 # 1번 팀이 이기고 있던 시간
teamWinTime2 = 0 # 2번 팀이 이기고 있던 시간
teamScore1 = 0 # 현재 1번 팀 점수
teamScore2 = 0 # 현재 2번 팀 점수
for i in range(0, timeToNum("48:00")): # 매 초마다 승자를 체크한다.
    if i in scoreDict:
        if scoreDict[i] == 1:
            teamScore1 += 1
        else:
            teamScore2 += 1
   
    if teamScore1 > teamScore2:
        teamWinTime1 += 1
    elif teamScore1 < teamScore2:
        teamWinTime2 += 1
        
print(numToTime(teamWinTime1))
print(numToTime(teamWinTime2))
'''
과제는 끝나지 않아!

입력
첫째 줄에 이번 학기가 몇 분인지를 나타내는 정수 N이 주어진다. (1 ≤ N ≤ 1,000,000)
두번째 줄부터 N줄 동안은 학기가 시작하고 N분째에 주어진 과제의 정보가 아래의 두 경우 중 하나로 주어진다.
1 A T: 과제의 만점은 A점이고, 성애가 이 과제를 해결하는데 T분이 걸린다. A와 T는 모두 정수이다. (1 ≤ A ≤ 100, 1 ≤ T ≤ 1,000,000)
0: 해당 시점에는 과제가 주어지지 않았다.

출력
성애가 받을 과제 점수를 출력한다.
'''

'''
- 문제에 적혀있는 그대로 구현만 하면 되는 문제이다.
* Fail/1st/00:08:42/IndexError
'''
import sys

def oneMinute():
    global currentTime, totalScore, allTask
    currentTime += 1
    
    (a, b) = allTask.pop()
    if a - 1 > 0:
        allTask.append((a - 1, b))
    else:
        totalScore += b

totalScore = 0
currentTime = 0
allTask = [] # (남은 분수, 점수)의 튜플로 구성

N = int(input())
for i in range(N):
    comText = sys.stdin.readline().rstrip()
    if comText[0] == "0":
        oneMinute()
    else:
        trash, score, time = map(int, comText.split())
        allTask.append((time, score))
        oneMinute()
        
print(totalScore)
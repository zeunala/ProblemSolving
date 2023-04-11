'''
주사위 쌓기

입력
첫줄에는 주사위의 개수가 입력된다. 그 다음 줄부터는 한 줄에 하나씩 주사위의 종류가 1번 주사위부터 주사위 번호 순서대로 입력된다.
주사위의 종류는 각 면에 적혀진 숫자가 그림1에 있는 주사위의 전개도에서 A, B, C, D, E, F 의 순서로 입력된다.
입력되는 숫자 사이에는 빈 칸이 하나씩 있다. 주사위의 개수는 10,000개 이하이며 종류가 같은 주사위도 있을 수 있다.


출력
첫줄에 한 옆면의 숫자의 합이 가장 큰 값을 출력한다.
'''

'''
- 1번 주사위는 아무거나 올 수 있으므로 밑면이 1~6이 오는 경우 각각에 대해 계산한다.
1번 주사위의 밑면이 우선 정해지면, 윗면은 자연스럽게 고정되고 2번 주사위부터의 윗면/밑면도 고정된다.
그 상태에서 윗면/밑면을 제외한 4개 면은 자유롭게 회전할 수 있으므로 각 주사위별 최댓값만 생각하면 된다.
* Pass/1st/00:14:38
'''
import sys

def getReverseSideNum(dice, target): # 여섯면이 주어지면 target의 반대편에 있는 숫자를 리턴한다.
    A, B, C, D, E, F = dice
    return {A: F, B: D, C: E, D: B, E: C, F: A}[target]

N = int(sys.stdin.readline().rstrip())
diceArr = []
answer = 0

for i in range(N):
    diceArr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
for i in range(1, 7): # 1번 주사위의 밑면이 1이 오는 경우 ~ 6이 오는 경우 각각에 대하여 계산
    tempAnswer = 0
    downSide = i # 밑면
    upSide = getReverseSideNum(diceArr[0], downSide) # 윗면
    tempAnswer += max([dice for dice in diceArr[0] if dice != downSide and dice != upSide]) # 1번 주사위 옆면중 최댓값
    
    # 2번 주사위부터 계산
    for j in range(1, N):
        downSide = upSide
        upSide = getReverseSideNum(diceArr[j], downSide)
        tempAnswer += max([dice for dice in diceArr[j] if dice != downSide and dice != upSide])
        
    if answer < tempAnswer:
        answer = tempAnswer
        
print(answer)
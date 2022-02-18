'''
야구

입력
첫째 줄에 이닝 수 N(2 ≤ N ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에는 각 선수가 각 이닝에서 얻는 결과가 1번 이닝부터 N번 이닝까지 순서대로 주어진다.
이닝에서 얻는 결과는 9개의 정수가 공백으로 구분되어져 있다. 각 결과가 의미하는 정수는 다음과 같다.

안타: 1
2루타: 2
3루타: 3
홈런: 4
아웃: 0
각 이닝에는 아웃을 기록하는 타자가 적어도 한 명 존재한다.

출력
아인타팀이 얻을 수 있는 최대 점수를 출력한다.
'''

'''
- 1번선수는 4번타자 고정이므로 나머지 8명만 최대 득점이 나오게 배치하면 된다. 8!=40320이므로 완전 탐색을 고려할 수 있다.
* Fail/1st/00:48:17/TimeOver
- 최적화가 좀 더 필요로 한 듯하다.
* Fail/2nd/01:20:18/TimeOver
- 첫번째 경우보단 테스트 케이스를 더 통과하였지만 아직 부족하다. hitDP배열을 추가하여 hitDP[a][b]를 필드 a에서 b루타를 쳤을 때 필드와 획득점수를 저장하도록 해보자.
* Fail/3rd/01:39:12/TimeOver
- 좀 더 최적화를 시도해보았다.
* Pass/4th/02:07:08(use PyPy3)
- (처음엔 시간초과가 났으나 재채점한 결과 시간초과가 나지 않아서 수정함)
'''
import sys
from itertools import permutations

hitDP = [[(0, 0) for _ in range(5)] for _ in range(8)] # hitDP[a][b]는 필드 a에서 b루타를 쳤을 때 필드와 획득점수를 저장함

def checkCase(playerOrder): # playerOrder는 선수 순서, scoreArr는 입력으로 주는 점수, turn은 총 이닝 수 해당 경우에 대한 점수를 리턴한다.
    resultScore = 0
    currentPlayer = -1 # 현재 치는 선수순서 (0번째부터 시작)

    for i in range(turn):
        field = 0 # 이진법으로 보아 000 > 주자 없음, 001 > 주자 1루, 110 > 주자 2/3루와 같이 본다.
        out = 0 # 아웃카운트

        while out < 3:
            currentPlayer = ((currentPlayer + 1) % 9)
            
            hitResult = scoreArr[i][playerOrder[currentPlayer]-1] # 현재 선수의 hit 결과
            if hitResult == 0:
                out += 1
            else:
                (field, getScore) = hitDP[field][hitResult]
                resultScore += getScore
    
    return resultScore

playerOrder = list(permutations([2,3,4,5,6,7,8,9])) # 여기에 경우의 수가 들어가며, 각 경우마다 1번을 4번자리에 넣으면 된다.
maximum = 0
turn = int(input()) # 이닝 수
scoreArr = [] # 각 이닝별 선수들의 결과
for i in range(turn):
    scoreArr.append(list(map(int, sys.stdin.readline().rstrip().split())))

# hitDP 세팅
for i in range(8): # i는 현재 필드
    for j in range(1, 5): # j는 몇 루타인지
        resultField = 0
        resultScore = 0

        field = i
        field = field << j
        field += (1 << (j-1))

        resultField = field % 8

        field = field >> 3
        while field > 0:
            resultScore += field % 2
            field = field >> 1
        
        hitDP[i][j] = (resultField, resultScore)    

for e in playerOrder:
    temp = checkCase(e[:3]+(1,)+e[3:]) # 각 경우마다 1번선수를 4번자리에 넣고 checkCase 함수를 돌린다.
    if temp > maximum:
        maximum = temp

print(maximum)
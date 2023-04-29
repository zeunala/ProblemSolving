'''
중간고사 채점

입력
첫째 줄에 문제의 개수 N과 응시자의 수 M이 주어진다. (1 ≤ N ≤ 100, 1 ≤ M ≤ 100)
둘째 줄에는 문제의 배점이 1번 문제부터 N번 문제까지 순서대로 주어진다.
각 문제의 배점은 100보다 작거나 같은 자연수이며, 공백으로 구분되어져 있다.
셋째 줄부터 M개의 줄에는 응시자의 정보가 한 줄에 하나씩 주어진다.
응시자의 정보는 총 N+1개의 문자열로 이루어져 있다. 첫 번째 문자열은 응시자의 수험 번호이다.
수험 번호는 100,000보다 작거나 같은 자연수이다. 두 번째 부터 N+1번째 문자열은 각 시험 문제의 채점 결과이다.
채점 결과는 1번 문제부터 N번 문제까지 순서대로 주어지며, 'O' 또는 'X'이다.
'O'가 주어진 경우에는 해당 문제를 맞춘 것이고, 'X'가 주어진 경우에는 해당 문제를 틀린 것이다.
문제를 맞춘 경우에는 그 문제의 배점이 점수에 더해지게 되며, 틀린 경우에는 더해지지 않는다. 수험 번호가 중복되는 경우는 없다.

출력
첫째 줄에 가장 높은 점수를 얻은 학생의 번호와 점수를 공백으로 구분해 출력한다.
만약, 가장 높은 점수를 얻은 학생이 여러 명이라면, 수험 번호가 가장 작은 것을 출력한다.
'''

'''
- N, M의 범위가 작으므로 문제의 요구사항을 그대로 구현한다.
* Fail/1st/00:09:46/RuntimeError
- 모든 사람이 틀렸을 때 playerScore가 완전히 빈 상태라 오류가 발생하는 문제를 수정하였다.
* Pass/2nd/00:12:16
'''
import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().rstrip().split())
scoreArr = list(map(int, sys.stdin.readline().rstrip().split())) # scoreArr[i]는 i번 문제의 점수(i>=0)
playerScore = defaultdict(int) # playerScore[i]는 i번 응시자의 점수

for i in range(M):
    nextLine = list(sys.stdin.readline().rstrip().split())
    currentNo = int(nextLine[0]) # 응시자 번호
    currentScore = 0
    
    for i in range(N):
        if nextLine[i + 1] == "O":
            currentScore += scoreArr[i]
    
    playerScore[currentNo] = currentScore
            
# 최대 점수의 응시자 번호를 구하되 수험 번호 작은 것이 우선
maxScore = max(playerScore.values())
for i in sorted(playerScore.keys()):
    if playerScore[i] == maxScore:
        print(i, maxScore)
        break
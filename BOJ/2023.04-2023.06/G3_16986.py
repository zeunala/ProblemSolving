'''
인싸들의 가위바위보

입력
첫째 줄에 인싸 가위바위보의 손동작 수를 나타내는 N(1 ≤ N ≤ 9)과 우승을 위해 필요한 승수 K(1 ≤ K ≤ 6)가 한 칸의 빈칸을 사이에 두고 주어진다.
그 다음 N개의 줄에 대해 상성에 대한 정보 Ai,j가 주어진다.
i+1번째 줄에는 N개의 정수 Ai,1, Ai,2, Ai,3, ..., Ai,N이 한 칸의 빈칸을 사이에 두고 주어진다.
Ai,j가 2일 경우에는 i번 손동작이 j번 손동작을 이긴다는 의미이고, 1일 경우에는 비긴다는 의미이고, 0일 경우에는 진다는 의미이다.
Ai,i = 1이고, i ≠ j일 때 Ai,j ≠ 1임이 보장된다. 또한 Ai,j가 2일 경우에는 Aj,i가 0이고, Ai,j가 0일 경우에는 Aj,i가 2임이 보장된다.
그 다음 줄에는 경희가 앞으로 자신이 참여하는 20경기에서 낼 손동작의 순서가 한 칸의 빈칸을 사이에 두고 주어진다.
손동작의 번호는 1 이상 N 이하이다.
그 다음 줄에는 민호가 앞으로 자신이 참여하는 20경기에서 낼 손동작의 순서가 한 칸의 빈칸을 사이에 두고 주어진다.
마찬가지로 손동작의 번호는 1 이상 N 이하이다.

출력
첫째 줄에 지우, 경희, 민호 순으로 경기를 진행할 때 지우가 모든 손동작을 다르게 내어 우승할 수 있으면 1을, 그렇지 않으면 0을 출력한다.
'''

'''
- 가능한 손동작이 최대 9개이므로, 모든 손동작을 다르게 내는 경우의 수는 최대 9! = 362880이다.
따라서 완전 탐색을 이용하여 가능한 모든 경우의 수에 대하여 우승하는 경우가 있는지 찾는다.
* Pass/1st/00:30:21
'''
import sys
from itertools import permutations

def canWin(arrA, K, mainPlayer, playerA, playerB): # 상성표와 승수, 플레이어별 내는 손동작이 주어졌을 때 우승할 수 있는지 리턴
    currentPlayer1 = 0 # 0이면 주인공, 1이면 A, 2면 B와 그 다음 사람이 가위바위보를 하는 차례
    currentPlayer2 = 1 # 0이면 주인공, 1이면 A, 2면 B와 그 다음 사람이 가위바위보를 하는 차례
    currentWinCount = [0, 0, 0] # 현재 몇승 중인지
    playerArr = [mainPlayer, playerA, playerB] # 주인공을 playerArr[0], A를 playerArr[1], B를 playerArr[2]로 하나로 합침
    playerIdx = [0, 0, 0] # 현재 낼 차례
    
    while True:
        if playerIdx[0] >= len(mainPlayer): # 주인공이 더 낼게 없으면 패배
            return False
        
        playResult = arrA[playerArr[currentPlayer1][playerIdx[currentPlayer1]] - 1][playerArr[currentPlayer2][playerIdx[currentPlayer2]] - 1]
        playerIdx[currentPlayer1] += 1
        playerIdx[currentPlayer2] += 1
        
        winnerPlayer = -1
        if playResult == 2 or (playResult == 1 and currentPlayer1 > currentPlayer2): # currentPlayer1이 이긴 경우
            winnerPlayer = currentPlayer1
        else: # currentPlayer2가 이긴 경우
            winnerPlayer = currentPlayer2
        
        currentWinCount[winnerPlayer] += 1
        if currentWinCount[winnerPlayer] >= K: # K승을 한 플레이어가 나왔을 경우
            if winnerPlayer == 0:
                return True
            else:
                return False
            
        # 다음 라운드에서는 전 라운드에서 안싸운 참가자 vs 전 라운드에서 우승한 참가자가 겨룬다.
        currentPlayer1 = (0 + 1 + 2) - (currentPlayer1 + currentPlayer2)
        currentPlayer2 = winnerPlayer

N, K = map(int, sys.stdin.readline().rstrip().split())
arrA = []
for i in range(N):
    arrA.append(list(map(int, sys.stdin.readline().rstrip().split())))
playerA = list(map(int, sys.stdin.readline().rstrip().split()))
playerB = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
for case in permutations(range(1, N + 1), N):
    if canWin(arrA, K, list(case), playerA, playerB):
        result = 1
        break
print(result)
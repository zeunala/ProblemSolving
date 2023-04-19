'''
가위 바위 보

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스의 첫째 줄에는 참여하는 로봇의 수 N이 주어진다.
다음 N개 줄에는 각 로봇에 저장되어 있는 문자열이 주어진다.
모든 로봇의 문자열의 길이는 k이다. (2 ≤ N ≤ 10, 3 ≤ k ≤ 30)
로봇은 주어지는 순서대로 1번부터 번호를 매긴다. 

출력
각 테스트 케이스마다, 게임을 승리한 로봇의 번호를 출력한다.
k 라운드가 지난 후에도 승자가 없는 경우 (무승부) 에는 0을 출력한다.
'''

'''
- N, k의 범위가 작으므로 문제의 요구사항을 그대로 구현한다.
* Pass/1st/00:14:48
'''
from collections import Counter

T = int(input())

for testCase in range(T):
    N = int(input())
    arr = []
    
    for i in range(N):
        arr.append(input())
        
    currentWinner = [i for i in range(N)] # 현재 남아있는 로봇들의 번호 (편의상 0번부터 시작)
    
    for round in range(len(arr[0])):
        if len(currentWinner) == 1:
            break
        
        roundAction = [arr[player][round] for player in currentWinner] # 현재 라운드에서 각 로봇들이 낸 가위/바위/보 상태
        allAction = Counter(roundAction).keys() # 로봇들이 낸 동작들
        if len(allAction) != 2: # 모든 남은 로봇들이 낸 동작이 딱 2개여야 탈락자가 갈라진다
            continue
        
        winAction = None # 이긴 사람이 낸 동작(가위/바위/보)
        if "S" not in allAction: # 바위/보만 있는 경우 - 보를 내야 이김
            winAction = "P"
        elif "R" not in allAction: # 가위/보만 있는 경우 - 가위를 내야 이김
            winAction = "S"
        elif "P" not in allAction: # 가위/바위만 있는 경우 - 바위를 내야 이김
            winAction = "R"
            
        currentWinner = [player for player in currentWinner if arr[player][round] == winAction] # 현재 남은 로봇 중 이긴걸 낸 로봇만 남음
        
    if len(currentWinner) == 1:
        print(currentWinner[0] + 1) # 편의상 처음 로봇을 0번으로 잡았었기 때문에 1을 더해야 함
    else:
        print(0)
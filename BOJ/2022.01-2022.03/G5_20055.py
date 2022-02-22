'''
컨베이어 벨트 위의 로봇

입력
첫째 줄에 N, K가 주어진다. 둘째 줄에는 A1, A2, ..., A2N이 주어진다.

출력
몇 번째 단계가 진행 중일때 종료되었는지 출력한다.
'''

'''
- 우선 N의 범위가 크지 않으므로 문제의 요구사항대로 구현을 해보자.
* Pass/1st/00:22:46(use PyPy3)
- 다른 사람의 풀이를 보고 생각해보니 어차피 upPos~downPos의 칸들만 신경쓰면 되고,
또 자연스럽게 downPos에 가까울 수록 먼저 올라갔을 것이므로 굳이 roboxIdx를 둘 필요 없이 탐색하면
좀 더 시간을 단축시킬 수 있을 것이다.
'''

N, K = map(int, input().split()) # N: 길이, K: 내구도 0 몇 개 이상이면 종료인지
A = list(map(int, input().split()))
arr = [[i, -1] for i in (A)] # (내구도, 로봇이 올라간 시간(없으면 -1))

upPos = 0 # 올리는 위치 (편의상 0~2N-1까지의 칸이 있다고 한다)
downPos = N - 1 # 내리는 위치
t = 0
while True:
    t += 1
    
    # 1단계: 벨트가 로봇과 함께 한 칸 회전 (upPos, downPos만 건들면 된다)
    upPos = (upPos - 1) % (2 * N)
    downPos = (downPos - 1) % (2 * N)
    if arr[downPos][1] != -1: # downPos에 로봇이 있다면 즉시 하차
        arr[downPos][1] = -1
        
    # 2단계: 가장 먼저 벨트에 올라간 로봇부터 회전 방향으로 한칸 이동
    robotIdx = [(arr[i][1], i) for i in range(len(arr)) if arr[i][1] != -1] # (로봇이 올라간 시간, 그 로봇의 위치)
    robotIdx.sort() # 먼저 올라온 것부터 정렬됨
    
    for (robotTime, robotPos) in robotIdx:
        nextRobotPos = (robotPos + 1) % (2 * N)
        if arr[nextRobotPos][1] == -1 and arr[nextRobotPos][0] > 0: # 다음 자리에 로봇 없고 내구도 존재
            arr[robotPos][1] = -1
            arr[nextRobotPos][1] = robotTime
            arr[nextRobotPos][0] -= 1
            
            if arr[downPos][1] != -1: # downPos에 로봇이 있다면 즉시 하차
                arr[downPos][1] = -1
            
    # 3단계: 올리는 위치의 내구도가 0이 아니면 로봇 올림
    if arr[upPos][0] > 0:
        arr[upPos][1] = t
        arr[upPos][0] -= 1
        
    # 4단계: 내구도가 0인 칸의 개수가 K개 이상이면 종료
    if len([i for i in range(len(arr)) if arr[i][0] == 0]) >= K:
        break
    

print(t)
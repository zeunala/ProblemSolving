'''
게임 개발

입력
첫째 줄에 건물의 종류 수 N(1 ≤ N ≤ 500)이 주어진다.
다음 N개의 줄에는 각 건물을 짓는데 걸리는 시간과 그 건물을 짓기 위해 먼저 지어져야 하는 건물들의 번호가 주어진다.
건물의 번호는 1부터 N까지로 하고, 각 줄은 -1로 끝난다고 하자.
각 건물을 짓는데 걸리는 시간은 100,000보다 작거나 같은 자연수이다.
모든 건물을 짓는 것이 가능한 입력만 주어진다.

출력
N개의 각 건물이 완성되기까지 걸리는 최소 시간을 출력한다.
'''

'''
- 각 건물들에 대하여 걸리는 시간은 해당 건물을 짓기 위한 사전 건물들의 시간 중 최댓값 + 해당 건물만 짓는 데 걸리는 시간이다.
조건이 없는 건물 부터 최소 시간을 계산하고, 계속해서 갱신해나가는 식으로 구현하면 될 것이다.
* Pass/1st/00:17:03
'''
N = int(input())
minTime = [100000000] * (N+1) # minTime[i]는 i번 건물을 짓기 위한 최소시간 (1번부터 시작)
timeSpend = [0] * (N+1)
needToBuild = [[] for _ in range(N+1)]

for i in range(N):
    inputList = list(map(int, input().split()))
    timeSpend[i+1] = inputList[0]
    needToBuild[i+1] = inputList[1:-1]
    if len(needToBuild[i+1]) == 0: # 조건이 없는 건물일 경우
        minTime[i+1] = inputList[0]
        
for i in range(N+2): # 건물의 수+1번 반복
    for i in range(1, N+1):
        if len(needToBuild[i]) > 0:
            minTime[i] = timeSpend[i] + max([minTime[i] for i in needToBuild[i]])

for i in range(1, N+1):
    print(minTime[i])
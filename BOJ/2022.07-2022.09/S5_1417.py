'''
국회의원 선거

입력
첫째 줄에 후보의 수 N이 주어진다.
둘째 줄부터 차례대로 기호 1번을 찍으려고 하는 사람의 수, 기호 2번을 찍으려고 하는 수, 이렇게 총 N개의 줄에 걸쳐 입력이 들어온다.
N은 50보다 작거나 같은 자연수이고, 득표수는 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 다솜이가 매수해야 하는 사람의 최솟값을 출력한다.
'''

'''
- 수의 범위가 작으므로 최대힙을 이용해서 최댓값 >= 현재득표수 일 경우 1명씩 뺏어오는 식으로 진행한다.
* Pass/1st/00:08:32
'''
import heapq

N = int(input())
currentScore = int(input())
answer = 0

arr = []
for i in range(N - 1):
    heapq.heappush(arr, -int(input())) # 입력받은 수를 최대힙에 입력

while arr: # 다른 후보가 존재하는 경우 루프 수행
    maxScore = -heapq.heappop(arr)
    
    if maxScore >= currentScore: # 다른 후보 중 최대값이 현재득표수 이상일 경우 1명을 뺏어온다.
        answer += 1
        currentScore += 1
        maxScore -= 1
        heapq.heappush(arr, -maxScore) # heappop 한 뒤 1을 뺀 값을 다시 heappush
    else: # 당선이 확정될 경우 루프 탈출
        break
    
print(answer)
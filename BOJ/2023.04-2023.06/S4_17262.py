'''
팬덤이 넘쳐흘러

입력
첫째 줄에 욱제의 열렬한 팬의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
둘째 줄부터 N개의 줄에 걸쳐, 각 줄에 정수 si, ei (1 ≤ si ≤ ei ≤ 100,000)가 순서대로 주어진다.
이는 i번째 팬이 학교에 있는 시간 [si, ei]을 의미한다.

출력
욱제가 학교에 머물러야 하는 최소의 시간을 출력한다.
'''

'''
- 가장 빨리 떠나는 사람의 떠난 시각 ~ 가장 늦게 온 사람의 온 시각만큼 욱제가 최소한 머물러야 한다.
만약 전자가 후자보다 뒤에 있다면 모든 사람이 머문 시간이 존재하므로 최소 시간은 0이다.
* Pass/1st/00:10:19
'''
import sys

N = int(sys.stdin.readline().rstrip())
startArr = [] # 팬들이 온 시각
endArr = [] # 팬들이 떠난 시각

for i in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    startArr.append(start)
    endArr.append(end)

fastestEnd = min(endArr) # 가장 빨리 떠난 사람의 시각
latestStart = max(startArr) # 가장 늦게 온 사람의 시각

if fastestEnd > latestStart:
    print(0)
else:
    print(latestStart - fastestEnd)
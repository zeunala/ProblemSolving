'''
수상 택시

입력
첫째 줄에 N과 M이 주어진다. (N ≤ 300,000, 3 ≤ M ≤ 10^9)
다음 N개 줄에는 각 사람이 상근이의 수상 택시를 타는 위치와 목적지가 주어진다. 모든 숫자는 0과 M 사이이다.

출력
첫째 줄에 상근이의 이동 거리의 최솟값을 출력한다.
'''

'''
- 우선 0->M으로 M만큼 이동하는 건 필수이고, 보트에 모든 사람을 태울 수 있으므로 오른쪽으로 이동하는 사람은 신경쓰지 않아도 된다.
문제는 왼쪽으로 이동하는 사람이 있는 경우로, 왼쪽으로 돌아갔다가 다시 그만큼 오른쪽으로 가야하므로 (뒤로 가는 거리)*2 만큼 추가된다.
이때, 2<-4, 3<-5와 같이 돌아가야 하는 거리가 겹칠 경우 둘을 한 번에 태웠다가 돌아가면 되므로 하나로 합칠 수 있다.
정리하면, 뒤로 가는 경우만 세고 중복되는 거리를 합쳐서 M + (총 뒤로 가야 하는 거리) * 2가 최솟값이 된다.
* Fail/1st/00:14:28
'''
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
goBack = [] # 뒤로 가야하는 경우 (도착점, 시작점)들의 집합, 예를 들어 (2, 5)는 5에서 2로 돌아가야 함을 의미

answer = M # 0 -> M까지는 무조건 이동해야 한다.
for i in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    if start < end:
        continue
    
    goBack.append((end, start))
    
goBack.sort() # 시작점이 앞에 있는 것 순으로 정렬한다.

lastStart = 0
lastEnd = 0
for (start, end) in goBack:
    # 되돌아 가는 지점이 겹치는 경우
    if lastEnd >= start:
        lastEnd = end
        continue
    
    answer += (lastEnd - lastStart) * 2
    lastStart = start
    lastEnd = end
answer += (lastEnd - lastStart) * 2

print(answer)
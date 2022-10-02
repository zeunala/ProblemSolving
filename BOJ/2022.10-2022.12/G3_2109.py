'''
순회강연

입력
첫째 줄에 정수 n이 주어진다. 다음 n개의 줄에는 각 대학에서 제시한 p값과 d값이 주어진다.

출력
첫째 줄에 최대로 벌 수 있는 돈을 출력한다.
'''

'''
- 우선 기간 d가 작은 순, d가 같다면 보수 p가 큰 순서로 정렬한다.
이후 하나씩 꺼내서 최소힙(p값기준)에 담는데 힙의 원소수보다 d가 크다면 그냥 넣고,
d가 같거나 작다면 최소힙에 있는 최솟값과 비교하여 현재 p값이 크다면 쫓아내고 새 원소를 최소힙에 넣도록 한다.
* Pass/1st/00:11:18
'''
import heapq
import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    p, d = map(int, sys.stdin.readline().rstrip().split())
    arr.append((p, d))
    
arr.sort(key = lambda x : (x[1], -x[0]))

heapArr = [] # 보수 p가 담긴 최소힙
for (p, d) in arr:
    if d > len(heapArr): # 시간이 여유로워 그냥 최소힙에 담아도 되는경우
        heapq.heappush(heapArr, p)
    elif p > heapArr[0]: # 최소힙에 자리는 없는데 현재 강연의 보수가 기존 것보다 큰 경우
        heapq.heappushpop(heapArr, p)

answer = 0
for e in heapArr:
    answer += e
print(answer)
'''
컵라면

입력
첫 줄에 숙제의 개수 N (1 ≤ N ≤ 200,000)이 들어온다.
다음 줄부터 N+1번째 줄까지 i+1번째 줄에 i번째 문제에 대한 데드라인과 풀면 받을 수 있는 컵라면 수가 공백으로 구분되어 입력된다.

출력
첫 줄에 동호가 받을 수 있는 최대 컵라면 수를 출력한다.
'''

'''
- 데드라인 기준 오름차순으로 정렬하고, 현재 최소힙의 크기 대비 데드라인이 남았다면 최소힙에 넣는다.
만약 데드라인이 남지 않았다면 최소힙의 최솟값보다 받을 수 있는 컵라면 수가 클 때만 교체하는 식으로 진행한다. 
* Pass/1st/00:06:47
'''
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
arr = [] # (데드라인, 컵라면 수)의 배열

for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append((a, b))
    
arr.sort()

currentHeap = [] # 받을 수 있는 컵라면 수들의 최소힙

for (a, b) in arr: # a: 데드라인, b: 받을 수 있는 컵라면 수
    if a > len(currentHeap):
        heapq.heappush(currentHeap, b)
    elif b > currentHeap[0]:
        heapq.heappushpop(currentHeap, b)
        
answer = 0
for i in currentHeap:
    answer += i
    
print(answer)
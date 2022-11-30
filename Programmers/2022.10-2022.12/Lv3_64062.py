'''
징검다리 건너기

- 건널 수 있는 사람의 수가 최대 k명이라면 k명까지는 OK이고 k+1명부터 건널 수 없으므로,
파라매트릭 서치를 이용하여 0~2억 범위를 좁혀나가도록 한다.
* Fail/1st/00:07:08
- k를 무시하고 코드를 작성한 부분이 문제였다.
k의 범위가 stones길이까지 가능하므로 아예 stones배열을 k개 범위내의 최댓값으로 정제한다.
k개 범위내의 최댓값 중 최솟값이 최대 건널 수 있는 친구들의 수가 된다.
* Pass/2nd/00:28:04
- 문제 풀이 이후 다른 사람의 풀이를 보니 그냥 파라매트릭 서치를 이용해서 연속 k개가 조건 불일치한지 체크해도 되는 것으로 보인다.
'''
import heapq
from collections import defaultdict
    
def solution(stones, k):
    stonesMax = [] # 연속k개의 최댓값들이 담길 배열
    stonesHeap = [] # 최댓값들을 담기 위한 힙
    stonesInHeapDict = defaultdict(int) # k개 내에 stone이 각 몇 개 있는지 저장
    
    # 첫 k개를 힙에 담고 최댓값 하나를 stonesMin에 담는다.
    for i in range(k):
        stonesInHeapDict[stones[i]] += 1
        heapq.heappush(stonesHeap, -stones[i])
    stonesMax.append(-stonesHeap[0])
    
    # 이후 최솟값들을 stonesMin에 담는다.
    for i in range(1, len(stones) - (k - 1)):
        stonesInHeapDict[stones[i - 1]] -= 1
        stonesInHeapDict[stones[i - 1 + k]] += 1
        heapq.heappush(stonesHeap, -stones[i - 1 + k])
        # 힙의 최솟값이 k개 범위 내에 존재해야한다.
        while stonesInHeapDict[-stonesHeap[0]] <= 0:
            heapq.heappop(stonesHeap)
        stonesMax.append(-stonesHeap[0])
    
    return min(stonesMax)
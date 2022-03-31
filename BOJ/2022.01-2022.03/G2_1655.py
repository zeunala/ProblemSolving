'''
가운데를 말해요

입력
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다.
N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다.
그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다.
정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.
'''

'''
- 각 정수마다 이진탐색을 통해 삽입하고, 중간값을 출력하도록 한다.
* Fail/1st/00:39:43/TimeOver
- 하나 하나 탐색하는 대신 파이썬의 bisect를 이용하는 방식으로 수정하였다.
* Fail/2nd/00:43:27/TimeOver
- 힙을 이용하는 방식으로 접근해보자.
최대힙과 최소힙을 만들어 최대힙에 삽입하되 최대힙과 최소힙의 원소 개수를 같거나 최대힙이 1개 크게 맞춰줘서,
최대힙에서 가장 큰 원소가 중간값이 되도록 만들면 된다.
* Fail/3rd/00:59:07
- 최대힙에 삽입할 때 최대힙의 최대원소보다 새로운 원소가 더 클 경우 최소힙의 최소원소와 교체해주어야지,
최대힙의 모든 원소가 최소힙의 모든 원소보다 작게 되어 조건을 만족할 수 있게 된다.
* Pass/4th/01:11:38
'''
import sys
import heapq

N = int(sys.stdin.readline().rstrip())

maxHeap = []
minHeap = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    
    # 우선적으로 최대힙에 삽입
    heapq.heappush(maxHeap, -num)
    
    # 새로 들어온 원소가 최대힙의 최댓값인데 이게 최소힙의 최솟값보다 큰 경우,
    # 최대힙의 모든 원소 < 최소힙의 모든 원소 조건을 맞추기 위해 원소를 교체한다.
    if len(minHeap) > 0 and -maxHeap[0] > minHeap[0]:
        tempA = -heapq.heappop(maxHeap)
        tempB = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, -tempB)
        heapq.heappush(minHeap, tempA)
    
    # 최대힙의 원소가 2개이상 많을 경우 크기를 맞춰준다.
    if len(maxHeap) >= len(minHeap) + 2:
        temp = -heapq.heappop(maxHeap)
        heapq.heappush(minHeap, temp)
    
    print(-maxHeap[0])
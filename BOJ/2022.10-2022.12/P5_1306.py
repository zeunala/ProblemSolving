'''
달려라 홍준

입력
첫째 줄에는 뛰는 코스의 길이, 즉 칸수 N과 홍준이의 시야의 범위 M이 주어진다.
시야가 M이라고 하면 현재 위치에서 앞뒤로 M-1칸까지 광고판이 보이는 것이다. (1 ≤ M ≤ N ≤ 1,000,000)
두 번째 줄에는 각각 칸에 있는 광고판들의 빛의 세기가 주어진다.
빛의 세기는 1,000,000을 넘지 않는 자연수이다.
홍준이는 언제나 광고판을 2M-1개 보면서 뛰고 싶기 때문에(중심으로)
M번째 칸에서 뛰기 시작해서 N-M+1번째 칸에서 멈춘다고 가정하자.

출력
뛰면서 보이는 광고판의 세기를 출력한다.
'''

'''
- 각 구간 별로의 최댓값을 알고 싶으므로 최대힙을 이용한다.
이 때, 시야에 벗어난 광고판의 세기를 보관해놨다가 최대힙의 값이 그것이라면 제외한다.
* Fail/1st/00:20:44
- 잘못 작성한 코드를 수정하였다.
* Pass/2nd/00:27:44
'''
import sys
import heapq

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

currentView = [] # 현재 보이는 시야에 대한 최대힙
removedView = [0] * 1000001 # 이미 지나쳐서 사라진 광고판의 세기들이 담김 (i번째 배열은 그 세기의 사라진 광고판 개수)


for i in range(2 * M - 1): # 초깃값 세팅
    heapq.heappush(currentView, -arr[i])
   
print(-currentView[0], end = " ")

for i in range(2 * M - 1, N):
    removedView[arr[i - (2 * M - 1)]] += 1 # 이미 지나쳐서 사라진 광고판의 세기
    heapq.heappush(currentView, -arr[i]) # 새로 들어온 광고판의 세기
    
    while removedView[-currentView[0]] > 0: # 만약 최댓값이 이미 사라진 광고판이었다면 그걸 제거해야한다.
        removedView[-currentView[0]] -= 1;
        heapq.heappop(currentView)
        
    print(-currentView[0], end = " ")

'''
보석 도둑

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
모든 숫자는 양의 정수이다.

출력
첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.
'''

'''
- 가방 무게로 오름차순, 보석 무게로 오름차순으로 정렬하고,
가벼운 가방부터 하나씩 확인하며, 넣을 수 있는 보석 중 가장 비싼 것부터 넣도록 하면 된다.
빠른 계산을 위해 무게를 1씩 늘리면서 가격을 최대힙에 저장해놓았다가, 가방 무게가 되었을 때 스택에서 가장 비싼 걸 꺼내도록 한다.
* Pass/1st/00:27:38
'''
import sys
import heapq

N, K = map(int, sys.stdin.readline().rstrip().split())
itemArr = [] # 각 보석의 (무게, 가격) 저장
bagArr = [] # 가방의 허용 무게 저장
answer = 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    itemArr.append((a, b))

for i in range(K):
    bagArr.append(int(sys.stdin.readline().rstrip()))
    
itemArr.sort()
bagArr.sort()

itemCheckIdx = 0 # 힙에 넣을 보석의 차례
bagCheckIdx = 0 # 보석을 넣을 가방의 차례
currentM = 0 # 현재 체크할 무게
tempHeap = []


while bagCheckIdx < len(bagArr):
    # 현재 currentM 무게 내의 보석들을 최대힙에 넣음
    if itemCheckIdx < len(itemArr) and currentM >= itemArr[itemCheckIdx][0]:
        heapq.heappush(tempHeap, -itemArr[itemCheckIdx][1])
        itemCheckIdx += 1
        continue
    
    # 현재 currentM 무게 내의 가방에 대하여 최대힙에서 보석을 꺼내 할당
    if currentM >= bagArr[bagCheckIdx]:
        if tempHeap:
            answer += -heapq.heappop(tempHeap)
        bagCheckIdx += 1
        continue
        
    currentM += 1
    
print(answer)
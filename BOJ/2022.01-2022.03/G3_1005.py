'''
ACM Craft

입력
첫째 줄에는 테스트케이스의 개수 T가 주어진다.
각 테스트 케이스는 다음과 같이 주어진다.
첫째 줄에 건물의 개수 N과 건물간의 건설순서 규칙의 총 개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다) 
둘째 줄에는 각 건물당 건설에 걸리는 시간 D1, D2, ..., DN이 공백을 사이로 주어진다.
셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. (이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다) 
마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.

출력
건물 W를 건설완료 하는데 드는 최소 시간을 출력한다.
편의상 건물을 짓는 명령을 내리는 데는 시간이 소요되지 않는다고 가정한다.
건설순서는 모든 건물이 건설 가능하도록 주어진다.
'''

'''
- 위상정렬을 하되, 우선순위 큐에 들어가는 기준이 해당 건물을 건설하는 데 걸리는 총 시간으로 둔다.
* Pass/1st/00:29:11
'''
import sys
import heapq

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N, K = map(int, sys.stdin.readline().rstrip().split()) # N: 건물 개수, K: 건설규칙 개수
    
    arrD = [0] + list(map(int, sys.stdin.readline().rstrip().split())) # 건물 하나 짓는데 걸리는 시간
    arrEdge = [[] for _ in range(N+1)] # 해당 건물 이후에 지어야 하는 건물들
    arrDegree = [0 for _ in range(N+1)] # 해당 건물 이전에 지어야 하는 건물 조건의 개수
    
    for j in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split()) # X 이후 Y를 지을 수 있음
        arrEdge[X].append(Y)
        arrDegree[Y] += 1
        
    W = int(sys.stdin.readline().rstrip()) # 목표 건물 번호
        
    heap = []
    for j in range(1, len(arrDegree)):
        if arrDegree[j] == 0:
            heapq.heappush(heap, (arrD[j], j)) # 조건이 없는 것들을 힙에 넣는다.

    while heap:
        times, num = heapq.heappop(heap) # 힙에서 가장 시간이 적게 걸리는 걸 꺼내온다. (times: 총 시간, num: 그 건물 번호)
        if num == W:
            print(times)
            break
        
        # 건물을 짓고 조건이 없어진 건물들의 정보를 힙에 추가
        for e in arrEdge[num]:
            arrDegree[e] -= 1
            if arrDegree[e] == 0:
                heapq.heappush(heap, (times + arrD[e], e))